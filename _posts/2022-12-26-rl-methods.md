---
title:  "Các phương pháp học tăng cường (RL-Methods)"
mathjax: true
layout: post
categories: RLMethods
---

![](https://nsanghi.com/assets/images/2021-02-07-deep-rl/mind_map_rl_algos.png)


## Tổng quan học tăng cường

Phương pháp học tăng cường được sử dụng để giải quyết lớp các bài toán/ chuỗi bài toán ra quyết định (decision problems) trong những môi trường thế giới thật thông qua các phương pháp/ mô hình ra quyết định (decision making) và học hướng về mục tiêu (goal-directed learning).

Học tăng cường được mô hình toán học hóa như một quá trình quyết định Markov (Markov Decision Process - MDP), được biết là mô hình toán học ra quyết định dạng chuỗi, trong đó những hành động (actions) tác động đến các phần thưởng ngắn hạn (tạm thời), các chuỗi trạng thái con (subsequent states) và phần thưởng tương lai.

Trong mô hình MDP, bài toán dự đoán và kiểm soát có thể được cài đặt thông qua việc sử dụng quy hoạch động (dynamic programming).

**Phát biểu bài toán**: MDP được định nghĩa bởi $$\{\mathcal{S}, \mathcal{A}, \mathcal{T}, \mathcal{R}, p(s_0), \gamma\}$$, trong đó:
- $$\mathcal{S}$$ là tập hợp của tất cả các trạng thái có thể có.
- $$\mathcal{A}$$ là tập hợp của những hành động mà có thể thích nghi trong các trạng thái.
- $$\mathcal{R}$$ là một ánh xạ, $$\mathcal{R}: \mathcal{S} \times \mathcal{A} \times \mathcal{S} \rightarrow \mathcal{R}$$, đại diện cho hàm phần thưởng (reward function), là những phần thưởng mà môi trường trả về cho tác tử sau khi thực hiện một hành động.
- $$\mathcal{T}$$ là một ánh xạ, $$\mathcal{T}: \mathcal{S} \times \mathcal{A} \rightarrow p(S)$$ được xác định bởi hàm chuyển trạng thái (state transition function)
- $$\gamma \in [0, 1]$$ đại diện cho hệ số chiết khấu (discount factor), đóng vai trò như một siêu tham số (hyperparameter) của tác tử (agent)

**Quá trình tương tác giữa tác tử và môi trường**: Trạng thái đầu tiên được lấy mẫu từ phân phối trạng thái khởi tạo (intial state distribution) $$p(s_0$$. Tại bước đi thứ $$t$$, tác tử thực hiện một quyết định tính toán dựa trên trạng thái $$s_t \in \mathcal{S}$$ được trả về từ môi trường và chọn hành động tương ứng $$a_t \in \mathcal{A}$$ mà sẽ được áp dụng vào môi trường, phụ thuộc vào sự thay đổi trong môi trường. Tác tử nhận được biểu diễn trạng thái $$s_{t+1} \sim \mathcal{T} (\cdot \mid s_t, a_t)$$ và một phần thưởng $$r_t = \mathcal{R}(s_t, a_t, s_{t+1})$$ tương ứngvới sự thay đổi trong môi trường. Tác nhân hành động trong môi trường dựa vào một chính sách $$\pi : \mathcal{S} \rightarrow p(\mathcal{A})$$. Bằng cách lặp lại việc lựa chọn hành động và dịch chuyển đến một trạng thái kế tiếp, một vết $$\{s_0, a_0, r_0, s_1, a_1, r_1, ...\}$$ được lấy mẫu từ môi trường.

![](https://pimages.toolbox.com/wp-content/uploads/2022/09/29100907/Reinforcement-Learning-Model.png)

Mục tiêu là tìm một chính sách (policy) $$\pi$$ mà cực đại trả về được kỳ vọng (expected return) $$Q(s,a)$$

$$
\pi^{*} = \underset{\pi}{\text{arg max}}Q(s,a) = \underset{\pi}{\text{arg max}}E_{\pi, \mathbb{T}}\left[\sum_{k=0}^K\gamma^kr_{t+k} | s_t = s, a_t = a\right]
$$

Phân loại thuật toán học tăng cường:
- Model-based: xây dựng trạng thái thể hiện mà mô hình nên dự đoán, các vấn đề tiềm năng giữa học đặc trưng (representation learning), học mô hình (model learning), và lên kế hoạch/ lập lịch (planning). Thách thức đối với nhóm mô hình này là việc mô hình hóa chưa thật sự hiệu quả trong môi trường thực tế.
- Model-free: các hướng tiếp cận còn lại.

## Q-learning

Q-Learning là một bộ học đóng chính sách (off-policy learner) và là phương pháp học Temporal Difference (Temporal Difference learning). Chính sách mục tiêu trong Q-learning cập nhật giá trị một cách trực tiếp trên Q-Table để mà đạt được lựa chọn chính sách tối ưu (optimal policy), trong khi đó chính sách hành vi (behavior policy) sử dụng chính sách $$\epsilon$$-greedy cho việc khá phá bán-ngẫu nhiên (semi-random exploration) của môi trường đang xem xét.

Mục tiêu học của hàm giá trị hành động (action-value function) $$Q$$ được học bởi trong Q-learning là hàm giá trị hành động tối ưu $$q^{*}$$. Hàm này được học bởi xấp xỉ trực tiếp

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha [R_{t+1} + \gamma\underset{a}{\text{max}}Q(s_{t+1},a) - Q(s_t,a_t)]
$$

Biểu thức trên thể hiện trạng thái $$s_t$$ khám phá môi trương với một chính sách hành vi dựa trên giá trị trong Q-table tại thời điểm $$t$$, tức là nó thực hiện một hành động $$a$$, phần thưởng $$R$$ và một trạng thái mới $$s_{t+1}$$ được nhận dựa trên phản hồi từ môi trường.

Biểu thức trên được thực thi để cập nhật rồi nhận được một Q-table mới nhất, nó sẽ tiếp tục cập nhật trạng thái mới $$s_{t+1}$$ sau khi hoàn thành quá trình cho đến khi chạm đến thời điểm dừng.

## REINFORCE

REINFORCE là một phương pháp không tối ưu hóa trực tiếp trên không gian chính sách nhưng học chính sách được tham số hóa không cần hàm ước lượng giá trị trực tiếp (intermediate value estimation function). Nó sử dụng phương pháp Monte Carlo cho việc học tham số chính sách với các trả về được ước lượng và vết đầy đủ (full trace).

Phương pháp tạo ra một chính sách dựa trên mạng neural mà nhận đầu vào là các trạng thái và sinh ra các phân phối xác suất trong không gian thực thi như đầu ra.

Mục tiêu của chính sách là cực đại hóa phần thưởng được kỳ vọng. Phần thưởng được chiết khấu được định nghĩa như tổng tất cả phần thưởng nhận được bởi tác tử trong tương lai.

Chính sách $$\pi$$ được tham số bởi một tập hợp của các trọng số $$\theta$$ mà $$\pi(s, \theta) \equiv \pi(s)$$, là phân phối xác suất hành động trên trạng thái. Biểu thức cập nhật của REINFORCE

$$
\Delta \omega_{i, j} = \alpha_{i, j}(r - b_{i, j})\frac{\vartheta}{\vartheta\omega_{i, j}}\text{ln}g_i
$$


## Actor-Critic

![](https://www.researchgate.net/profile/Taiki-Fuji/publication/322677430/figure/fig5/AS:586281910292487@1516791908629/Actor-critic-method.png)

## Bernoulli Multi-armed Bandit

![](https://leovan.me/images/cn/2020-05-16-multi-armed-bandit/compulsive-gambling.png)


## Neural Fitted Q-iteration


## Deep Q-learning Network

![](https://www.researchgate.net/profile/Huang-Chongwen/publication/339471857/figure/fig1/AS:862314022596609@1582603092955/a-An-illustration-of-deep-Q-learning-where-a-double-DNN-to-approximate-the-optimal.png)


## Double DQN

![](https://www.researchgate.net/profile/Mohit-Sewak/publication/345711318/figure/fig1/AS:956555692367872@1605072057186/Architecture-for-DQN-and-Double-DQN.ppm)


## Advantage Actor-Critic

![](https://www.researchgate.net/profile/Lorenzo-Federici/publication/343639364/figure/fig5/AS:925509202505735@1597669997770/Schematic-of-the-Advantage-Actor-Critic-RL-process-for-a-deterministic-MDP.png)


## Asynchronous Advantage Actor-Critic

![](https://www.researchgate.net/publication/347395657/figure/fig5/AS:1020918159650818@1620417265786/Asynchronous-Advantage-Actor-Critic-A3C-framework.png)


## Deep Deterministic Policy Gradient

![](https://www.researchgate.net/publication/338552761/figure/fig3/AS:846869919956992@1578920931494/Deep-Deterministic-Policy-Gradient-DDPG-algorithm-structure.png)


## Proximal Policy Optimization

![](https://intellabs.github.io/coach/_images/ppo.png)


## Cascaded DQN


**References**

[1] Watkins, C. J., & Dayan, P. (1992). [Q-learning](https://link.springer.com/article/10.1007/BF00992698). Machine learning, 8(3), 279-292.

[2] Williams, R. J. (1992). [Simple statistical gradient-following algorithms for connectionist reinforcement learning](https://link.springer.com/article/10.1007/BF00992696). Machine learning, 8(3), 229-256.

[3] Konda, V., & Tsitsiklis, J. (1999). [Actor-critic algorithms](https://proceedings.neurips.cc/paper/1999/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html). Advances in neural information processing systems, 12.

[4] Vermorel, J., & Mohri, M. (2005, October). [Multi-armed bandit algorithms and empirical evaluation](https://link.springer.com/chapter/10.1007/11564096_42). In European conference on machine learning (pp. 437-448). Springer, Berlin, Heidelberg.

[5] Riedmiller, M. (2005, October). [Neural fitted Q iteration–first experiences with a data efficient neural reinforcement learning method](https://link.springer.com/chapter/10.1007/11564096_32). In European conference on machine learning (pp. 317-328). Springer, Berlin, Heidelberg.

[6] Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness, J., Bellemare, M. G., ... & Hassabis, D. (2015). [Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236?wm=book_wap_0005). nature, 518(7540), 529-533.

[7] Van Hasselt, H., Guez, A., & Silver, D. (2016, March). [Deep reinforcement learning with double q-learning](https://ojs.aaai.org/index.php/AAAI/article/view/10295). In Proceedings of the AAAI conference on artificial intelligence (Vol. 30, No. 1).

[8] Mnih, V., Badia, A. P., Mirza, M., Graves, A., Lillicrap, T., Harley, T., ... & Kavukcuoglu, K. (2016, June). [Asynchronous methods for deep reinforcement learning](http://proceedings.mlr.press/v48/mniha16.html?ref=https://githubhelp.com). In International conference on machine learning (pp. 1928-1937). PMLR.

[9] Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., ... & Wierstra, D. (2015). [Continuous control with deep reinforcement learning](https://arxiv.org/pdf/1509.02971.pdf). arXiv preprint arXiv:1509.02971.

[10] Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). [Proximal policy optimization algorithms](https://arxiv.org/abs/1707.06347). arXiv preprint arXiv:1707.06347.

[11] Chen, X., Li, S., Li, H., Jiang, S., Qi, Y., & Song, L. (2019, May). [Generative adversarial user model for reinforcement learning based recommendation system](http://proceedings.mlr.press/v97/chen19f.html). In International Conference on Machine Learning (pp. 1052-1061). PMLR.

