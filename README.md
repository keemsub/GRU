# AI Challenge - Spatio-Temporal Data Prediction

## 대회 설명

- 시공간 데이터는 교통, 물류, 에너지 등 다양한 산업분야에서 광범위하게 발생하게 있으며,

  미래에 발생할 데이터를 미리 예측하는 것은 경제/산업적 측면에서의 활용가치가 매우 높음

- 전통적인 통계적 시계열 예측 모델은 다양한 속성값을 동시에 잘 활용하지 못하며,

  특별히 데이터의 공간적 상관관계를 분석하지 못하여 매우 예측 정확도가 떨어지는 한계점이 존재함

- 인하대학교 인공지능융합연구센터에서는 본 챌린지를 통해 풍력 발전소의 전기 에너지 발생량에 대한 데이터를 분석하여

미래에 기대되는 에너지 발생량을 높은 정확도로 예측하는 인공지는 모델 개발을 목표로 함

- 해당 모델은 에너지 분야 뿐만 아니라 교통 및 물류 분야의 다양한 시공간 데이터에 적용할 수 있을 것으로 기대됨


## 평가
1) 평가 산식 및 평가 규제

<img width="504" alt="20230125_204238" src="https://user-images.githubusercontent.com/88781717/214554811-81a48127-aaa5-4032-a21f-b5228d3a83c0.png">


- 특정 시간에 측정되지 않은 경우, 해당 Patv에 대하여 Error = 0

- 특정 시간에 측정된 Feature의 값이 Patv ≤ 0 and Wspd > 2.5인 경우, Patv 에 대하여 Error = 0

- 특정 시간에 측정된 Feature의 값이 Pab1 > 89° or Pab2 > 89° or Pab3 > 89°인 경우,

Patv에 대하여 Error = 0

- 특정 시간에 측정된 Feature의 값이 Ndir > 720° or Ndir < -720°인 경우 Patv에 대하여 Error = 0

- 특정 시간에 측정된 Feature의 값이 Wdir > 180° or Wdir < -180°인 경우, Patv에 대하여 Error = 0

(※ Error = 실제 값 - 예측 값)


 이하..https://dacon.io/competitions/official/235952/overview/description 참고

