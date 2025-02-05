# Granger Causality Equations

## 1. **Restricted Model**
The restricted model predicts $Y_{t}$ using only its own past values:

$Y_{t} = \alpha_{0} + \sum_{i=1}^{p} \alpha_i Y_{t-i} + \epsilon_{t}$

- $Y_t$: Target variable at time $t$.
- $\alpha_0$: Constant term.
- $\alpha_i$: Coefficients for the lagged values of $Y$.
- $p$: Number of lags for $ Y $.
- $\epsilon_t$: Error term.

---

## 2. **Unrestricted Model**
The unrestricted model predicts $Y_t$ using both its own past values and the past values of $X$:

$Y_t = \alpha_0 + \sum_{i=1}^{p} \alpha_i Y_{t-i} + \sum_{j=1}^{q} \beta_j X_{t-j} + \epsilon_t$

- $X_{t-j}$: Predictor variable at lag $j$.
- $\beta_j$: Coefficients for the lagged values of $X$.
- $q$: Number of lags for $X$.

---

## 3. **Hypothesis Testing**
The null hypothesis $H_0$ is that $X$ does not Granger-cause $Y$, meaning all $\beta_j = 0$:

$H_0: \beta_1 = \beta_2 = \dots = \beta_q = 0$

The alternative hypothesis $H_1$ is that at least one $\beta_j \neq 0$, indicating $X$ Granger-causes $Y$.

---

## 4. **Test Statistic (F-Test)**
The F-statistic compares the residual sum of squares (RSS) from the restricted and unrestricted models:

$F = \frac{(RSS_{\text{restricted}} - RSS_{\text{unrestricted}}) / q}{RSS_{\text{unrestricted}} / (T - p - q - 1)}$

- $RSS_{\text{restricted}}$: Residual sum of squares from the restricted model.
- $RSS_{\text{unrestricted}}$: Residual sum of squares from the unrestricted model.
- $T$: Number of observations.
- $p$: Number of lags for $ Y $.
- $q$: Number of lags for $ X $.

---

## 5. **Decision Rule**
- If the F-statistic > critical value (from the F-distribution), reject $H_0 .
- Conclude that $X$ Granger-causes $Y$.

---

## References
1. Granger, C. W. J. (1969). "Investigating Causal Relations by Econometric Models and Cross-Spectral Methods." *Econometrica*.
2. Hamilton, J. D. (1994). *Time Series Analysis*. Princeton University Press.
3. Enders, W. (2014). *Applied Econometric Time Series*. Wiley.