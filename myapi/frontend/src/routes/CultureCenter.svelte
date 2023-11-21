<!-- CultureCenter.svelte -->

<script>
    // facilities 가져오기
    import { facilities } from '../lib/facilities.js';
  </script>
  
  <style>

    h3 {
      font-family: 'Jua', sans-serif;
      text-align: center;
      margin-top: 15px;
    }

    .card-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      margin: 40px 20px 0;
    }
  
    .card {
      width: calc(20% - 10px);
      margin-bottom: 20px;
      margin-left: 20px;
      margin-right: 20px;
      /* 다른 카드 스타일링 속성들 */
      border: 1.5px solid #ff77a0;
    }
  
    /* 미디어 쿼리를 이용한 반응형 스타일 */
    @media screen and (max-width: 1200px) {
      .card {
        width: calc(25% - 10px);
      }
    }
  
    @media screen and (max-width: 992px) {
      .card {
        width: calc(33.33% - 10px);
      }
    }
  
    @media screen and (max-width: 768px) {
      .card {
        width: calc(50% - 10px);
      }
    }
  
    @media screen and (max-width: 576px) {
      .card {
        width: 100%;
      }
    }
  </style>
  
  <!-- 카드들을 담을 컨테이너 -->
  <h3>강남구 반려동물 동반 가능 문화시설 및 식당</h3>
  <div class="card-container" style="font-family: 'Jua', sans-serif;">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">
    {#each facilities as facility}
      <div class="card" style="width: 18rem;">
        <div class="card-body">
          <h4 class="card-title">{facility.시설명}</h4>
          <h6 class="card-subtitle mb-2 text-muted">{facility.카테고리3}</h6>
          <p class="card-text">주소: {facility.도로명주소}</p>
          <p class="card-text">전화번호: {facility.전화번호}</p>
        </div>
      </div>
    {/each}
  </div>
  <footer>
    <hr>
    <p> &nbsp; Copyright © 2023 Yeon Jae Park. All rights reserved.</p>
    <address> &nbsp; Contact email for more information. naver@naver.com</address>
    <style>
      footer {
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: left;
        background-color: #fffdfa;
        font-size: 12px,
        margin: 0;
      }
      footer hr {
        margin-top: 120px;
      }
    </style>
  </footer>

