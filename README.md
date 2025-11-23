## 2025.11.23(일) 파이썬 12주차 과제(문제 32번 ~ 38번)

# 1. commit 방식
문제 풀이 완료 후 git으로 커밋

커밋 메시지 : "feat: 파이썬 12주차 과제(문제 32번 ~ 38번)"

커밋 후 git_hub 저장소에 push/pull 하여 제출

# 2. 파일 구성
'2501045.py' = 파이썬 32번 ~ 38번 문제 풀이 작성한 코드

'READEME.md' = 과제 설명

# 3. 코드 설명
**set : 집합을 표현하는 세트, {} 안에 값을 저장**를 활용한 과제

**집합연산** 내장 함수
**1. 합집합(union) : 세트1 | 세트2, set.union(세트1, 세트2)**
**2. 교집합(intersection) : 세트1 & 세트2, set.intersection(세트1, 세트2)**
**3. 차집합(difference) : 세트1 - 세트2, set.difference(세트1, 세트2)**
**4. 대칭자집합(symmetric difference) : 세트1 ^ 세트2, set.symmetric_difference(세트1, 세트2)**
**5. Update 메서드**
  **1) update : 세트1 |= 세트2, 세트1.update(세트2)**
  **2) intersection_update : 세트1 &= 세트2, 세트1.intersection_update(세트2)**
  **3) difference_update : 세트1 -= 세트2, 세트1.difference_update(세트2)**
  **4) symmetric_difference_update : 세트1 ^= 세트2, 세트1.symmertric_difference_update(세트2)**
**6. 부분집합(subset) : issubset 메서드와 동일, 현재세트 <= 다른세트, 현재세트.issubset(다른세트)**
**7. 진부분집합(proper subset) : 현재세트 < 다른세트**
**8. 상위집합(superset) : 현재세트 >= 다른세트, 현재세트.issuperset(다른세트)**
**9. 진상위집합(proper superset) : 현재세트 > 다른세트**

## 4. 기타 정보

* **학과 및 작성자(학번):** 스마트 IT과 강서경(2501045)
  
* **작성일:** 2025. 11. 23(일)
