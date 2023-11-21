<script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'
    import { page, keyword, is_login } from "../lib/store"
    import moment from 'moment/min/moment-with-locales'
    moment.locale('ko')

    let question_list = []
    let size = 10
    //let page = 0
    let total = 0
    let kw = ''
    $: total_page = Math.ceil(total/size)

    function get_question_list() {
        let params = {
            page: $page,
            size: size,
            keyword: $keyword,
        }
        fastapi('get', '/api/question/list', params, (json) => {
            question_list = json.question_list
            total = json.total
            kw = $keyword
        })
    }

    $:$page, $keyword, get_question_list()


    import { onMount } from 'svelte';
  
  let currentAd = 0; // 현재 광고 이미지 인덱스
  let adImages = [
    'https://cdn.pixabay.com/photo/2023/11/19/05/58/cat-8398006_1280.png',
    'https://cdn.pixabay.com/photo/2023/11/19/06/03/06-03-08-553_1280.png',
    'https://cdn.pixabay.com/photo/2023/11/19/06/03/06-03-08-601_1280.png'
  ]; // 여러 개의 광고 이미지 URL
  
  onMount(() => {
    // 5초마다 이미지 변경
    const interval = setInterval(() => {
      currentAd = (currentAd + 1) % adImages.length;
    }, 5000);
    
    // 컴포넌트가 파괴될 때 인터벌 해제
    return () => clearInterval(interval);
  });
</script>

<div class="container my-3" style="font-family: 'Jua', sans-serif;">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">


    <div class="row my-3">
        <div class="col-6">
            <a use:link href="/question-create" 
                class="btn btn-primary {$is_login ? '' : 'disabled'}">글쓰기</a>
        </div>
        <div class="col-6">
            <div class="input-group">
                <input type="text" class="form-control" bind:value="{kw}">
                <button class="btn btn-outline-secondary" on:click={() => {$keyword = kw, $page =0}}>
                    검색
                </button>
            </div>
        </div>
    </div>

    
    <div class="row my-3">
        <div class="col-12 text-center">
            <img src={adImages[currentAd]} alt="Ad Banner" width="900" height="350" style="max-width: 100%;">
        </div>
    </div>

    <table class="table">
        <thead>
        <tr class="text-center table-warning">
            <th>번호</th>
            <th style="width:50%">제목</th>
            <th>작성자</th>
            <th>작성일시</th>
        </tr>
        </thead>
        <tbody>
        {#each question_list as question, i}
        <tr class="text-center">
            <td>{ total - ($page * size) - i }</td>
            <td class="text-start">
                <a use:link href="/detail/{question.id}">{question.subject}</a>
                {#if question.answers.length >0}
                <span class="text-danger small mx-2">{question.answers.length}</span>
                {/if}
            </td>
            <td>{ question.user ? question.user.username : "" }</td>
            <td>{moment(question.create_date).format("YYYY년 MM월 DD일 hh:mm a")}</td>
        </tr>
        {/each}
        </tbody>
    </table>


    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
        <style>
            /* 페이지네이션 버튼의 배경색과 활성화된 버튼의 배경색을 변경합니다 */
            .page-link {
                background-color: #FFC0CB;
                border-color: #FFC0CB;
                color: #fff; /* 버튼 글자 색상을 변경할 수 있습니다 */
            }
        
            /* 활성화된 페이지 버튼의 배경색을 변경합니다 */
            .page-item.active .page-link {
                background-color: #FFC0CB;
                border-color: #FFC0CB;
            }
        
            /* 비활성화된 버튼의 스타일을 변경합니다 */
            .page-item.disabled .page-link {
                pointer-events: none; /* 클릭 비활성화 */
                background-color: #e9ecef;
                border-color: #e9ecef;
                color: #6c757d;
            }
        </style>
        <!-- 이전페이지 -->
        <li class="page-item {$page <= 0 && 'disabled'}">
            <button class="page-link" on:click="{() => get_question_list($page--)}">이전</button>
        </li>
        <!-- 페이지번호 -->
        {#each Array(total_page) as _, loop_page}
        {#if loop_page >= $page-5 && loop_page <= $page+5} 
        <li class="page-item {loop_page === $page && 'active'}">
            <button on:click="{() => $page = loop_page}" class="page-link">{loop_page+1}</button>
        </li>
        {/if}
        {/each}
        <!-- 다음페이지 -->
        <li class="page-item {$page >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{() => $page++}">다음</button>
        </li>
    </ul>
    <!-- 페이징처리 끝 -->
</div>

<footer>
    <hr>
    <p> &nbsp; Copyright © 2023 Yeon Jae Park. All rights reserved.</p>
    <address> &nbsp; Contact email for more information. naver@naver.com</address>
</footer>
<style>
    footer {
    /* position: fixed; */
    bottom: 0;
    left: 0;
    width: 100%;
    text-align: left;
    background-color: #fffdfa;
    font-size: 12px;
    margin: 0;
}
footer hr {
        margin-top: 120px; /* 아래로 내리고 싶은 만큼 조절 */
    }
</style>


