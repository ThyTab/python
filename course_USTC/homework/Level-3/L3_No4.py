"""
4.
列文伯格-马夸尔特算法（Levenberg-Marquardt Algorithm）
用于求解非线性最小二乘问题
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False      #防止中文乱码

class LevenbergMarquardt:
    #列文伯格-马夸尔特算法
    
    def __init__(self, max_iter=100, tau=1e-3, eps1=1e-9, eps2=1e-9):
        self.max_iter = max_iter
        self.tau = tau          # 初始阻尼因子
        self.eps1 = eps1         # 梯度阈值
        self.eps2 = eps2         # 参数阈值
        self.history = []        # 记录迭代过程
    
    def fit(self, f, J, params0):
        #f: 残差函数 f(params) 返回残差向量
        #J: 雅可比矩阵函数 J(params) 返回雅可比矩阵
        #params0: 初始参数
        #return: 最优参数
        
        params = np.array(params0, dtype=float).flatten()
        n = len(params)
        
        # 计算初始残差和雅可比矩阵
        residuals = f(params)
        J_mat = J(params)
        
        # 初始化阻尼因子
        mu = self.tau * np.max(np.diag(J_mat.T @ J_mat))
        nu = 2
        
        self.history = [{
            'iter': 0,
            'params': params.copy(),
            'error': np.sum(residuals**2),
            'mu': mu
        }]
        
        print("=" * 60)
        print("列文伯格-马夸尔特算法")
        print("=" * 60)
        print(f"{'迭代':^6} {'误差':^15} {'μ':^15} {'参数变化':^15}")
        print("-" * 60)
        
        for i in range(self.max_iter):
            # 计算梯度
            grad = J_mat.T @ residuals
            grad_norm = np.linalg.norm(grad)   #计算范数          
            # 检查收敛条件：梯度足够小
            if grad_norm < self.eps1:
                print(f"{'收敛':^6} - 梯度范数: {grad_norm:.2e}")
                break
            
            # 尝试更新
            H = J_mat.T @ J_mat + mu * np.eye(n)
            try:
                delta = -np.linalg.solve(H, grad)   #求解方程
            except np.linalg.LinAlgError:
                mu *= nu
                nu *= 2
                continue
            
            # 计算增益比判断是否接受更新
            params_new = params + delta
            residuals_new = f(params_new)
            error_new = np.sum(residuals_new**2)
            error_old = np.sum(residuals**2)
            rho = (error_old - error_new) / (delta @ (mu * delta - grad))
            
            if rho > 0:
                params = params_new
                residuals = residuals_new
                J_mat = J(params)
                mu *= max(1/3, 1 - (2*rho - 1)**3)
                nu = 2
                param_change = np.linalg.norm(delta)
                error = error_new
                
                # 检查收敛条件：参数变化足够小
                if param_change < self.eps2 * (np.linalg.norm(params) + self.eps2):
                    print(f"{'收敛':^6} - 参数变化: {param_change:.2e}")
                    self.history.append({
                        'iter': i + 1,
                        'params': params.copy(),
                        'error': error,
                        'mu': mu
                    })
                    print(f"{i+1:^6} {error:^15.6f} {mu:^15.6e} {param_change:^15.6e}")
                    break
            else:
                mu *= nu
                nu *= 2
                param_change = 0
                error = error_old
                continue  # 跳过本次迭代，不记录不打印
            
            self.history.append({
                'iter': i + 1,
                'params': params.copy(),
                'error': error,
                'mu': mu
            })
            print(f"{i+1:^6} {error:^15.6f} {mu:^15.6e} {param_change:^15.6e}")
        
        print("=" * 60)
        print(f"最终误差: {self.history[-1]['error']:.6f}")
        print(f"最终参数: {params}")
        
        return params
    
    def plot_convergence(self):
        """绘制收敛曲线"""
        errors = [h['error'] for h in self.history]
        
        plt.figure(figsize=(10, 5))
        plt.semilogy(errors, 'b-o', markersize=4)
        plt.xlabel('迭代次数')
        plt.ylabel('误差 (log scale)')
        plt.title('L-M 算法收敛曲线')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()


def example_curve_fitting():
    """
    示例：曲线拟合
    拟合 y = a * exp(-b * x) + c
    """
    print("\n" + "=" * 60)
    print("示例：非线性曲线拟合")
    print("真实模型: y = 2 * exp(-0.5 * x) + 1")
    print("=" * 60 + "\n")
    
    # 生成带噪声的数据
    np.random.seed(42)
    x = np.linspace(0, 10, 50)
    y_true = 2 * np.exp(-0.5 * x) + 1
    y_noisy = y_true + np.random.normal(0, 0.2, len(x))
    
    # 定义残差函数
    def residuals(params, x, y):
        a, b, c = params
        return y - (a * np.exp(-b * x) + c)
    
    # 定义雅可比矩阵
    def jacobian(params, x, y):
        a, b, c = params
        J = np.zeros((len(x), 3))
        J[:, 0] = -np.exp(-b * x)           # ∂r/∂a
        J[:, 1] = a * x * np.exp(-b * x)    # ∂r/∂b
        J[:, 2] = -1                         # ∂r/∂c
        return J
    
    # 运行 LM 算法
    lm = LevenbergMarquardt(max_iter=100)
    params = lm.fit(lambda p: residuals(p, x, y_noisy), 
                     lambda p: jacobian(p, x, y_noisy), 
                     params0=[1.0, 1.0, 0.0])
    
    print(f"\n真实参数: a=2.0, b=0.5, c=1.0")
    print(f"拟合参数: a={params[0]:.4f}, b={params[1]:.4f}, c={params[2]:.4f}")
    
    # 绘图：曲线拟合结果
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y_noisy, c='blue', alpha=0.6, label='带噪声数据')
    plt.plot(x, y_true, 'g--', linewidth=2, label='真实曲线')
    y_fit = params[0] * np.exp(-params[1] * x) + params[2]
    plt.plot(x, y_fit, 'r-', linewidth=2, label='拟合曲线')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('曲线拟合结果')
    plt.grid(True, alpha=0.3)
    
    # 绘图：收敛曲线
    lm.plot_convergence()
    plt.show()


if __name__ == "__main__":
    example_curve_fitting()
