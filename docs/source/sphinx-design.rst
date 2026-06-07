sphinx-design
===================================


.. card:: 对偶向量

   对偶向量是从向量空间 :math:`V` 到 :math:`\mathbb{R}` 的线性映射。

   +++
   .. button-ref:: dual_space
      :color: primary
      :expand:

      了解更多

.. grid:: 2

   .. grid-item-card:: 向量
      :margin: 2 2 0 0

      几何对象，不依赖于坐标系

   .. grid-item-card:: 对偶向量
      :margin: 2 2 0 0

      线性泛函，同样不依赖于坐标系

   .. grid-item-card:: 分量
      :margin: 2 2 0 0

      依赖于坐标系的选择

   .. grid-item-card:: 基向量
      :margin: 2 2 0 0

      依赖于坐标系的选择

.. tab-set::

   .. tab-item:: 抽象定义

      .. math::

         \alpha: V \rightarrow \mathbb{R}

   .. tab-item:: 分量形式

      .. math::

         \alpha(\vec{v}) = \sum_{i=1}^{n} \alpha_i v^i

   .. tab-item:: 矩阵形式

      .. math::

         \begin{bmatrix} \alpha_1 & \alpha_2 & \cdots & \alpha_n \end{bmatrix} \begin{bmatrix} v^1 \\ v^2 \\ \vdots \\ v^n \end{bmatrix}


.. dropdown:: 证明：对偶空间是向量空间

   :animate: fade-in

   需要验证以下公理：

   - 加法封闭性
   - 数乘封闭性
   - 零元存在
   - 逆元存在

   .. math::

      (\alpha + \beta)(\vec{v}) = \alpha(\vec{v}) + \beta(\vec{v})


:bdg-primary:`线性代数` :bdg-success:`张量分析` :bdg-warning:`重要概念`

:bdg-primary-line:`定义` :bdg-success-line:`定理` :bdg-danger-line:`注意`


.. button-link:: https://en.wikipedia.org/wiki/Dual_space
   :color: primary
   :expand:

   维基百科：对偶空间

.. button-link:: #
   :color: secondary
   :outline:

   返回顶部

.. grid:: 1 1 2 2

   .. grid-item::

      **向量**

      向量是几何对象，独立于坐标系。

   .. grid-item::

      **对偶向量**

      对偶向量也是几何对象，独立于坐标系。

      .. math::

         \alpha(\vec{v}) \in \mathbb{R}








