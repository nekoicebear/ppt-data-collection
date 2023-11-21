<script>
    import { link } from 'svelte-spa-router'
    import { page, keyword, access_token, username, is_login } from "../lib/store"
</script>

<!-- 네비게이션바 -->
<style>
    .navbar-custom {
        background-color: #ffae008e; /* 배경 색상을 원하는 색상으로 지정하세요. */
    }
</style>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bagel+Fat+One&display=swap" rel="stylesheet">

<nav class="navbar navbar-expand-lg navbar-light navbar-custom border-bottom">
    <div class="container-fluid">
        <!-- <img src="https://cdn.pixabay.com/photo/2022/03/29/15/02/cat-7099550_1280.png" alt="Logo" width="25" height="30"> -->
        <a use:link class="navbar-brand" href="/" on:click="{() => {$keyword = '', $page =0 }}" style="font-family: 'Bagel Fat One', sans-serif;">고양이 커뮤니티</a>
        <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation">
            <span class="navbar-toggler-icon">
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent" style="font-family: 'Jua', sans-serif;" >
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">
            
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                {#if $is_login }
                    <li class="nav-item">
                        <a use:link href="/user-login" class="nav-link" on:click={() => {
                            $access_token = ''
                            $username = ''
                            $is_login = false
                        }}>로그아웃 ({$username})</a>
                    </li>
                    <li class="nav-item">
                        <a use:link class="nav-link" href="/pet-culture-center">강남구 문화시설</a>
                    </li>
                {:else}
                    <li class="nav-item">
                        <a use:link class="nav-link" href="/user-create">회원가입</a>
                    </li>
                    <li class="nav-item">
                        <a use:link class="nav-link" href="/user-login">로그인</a>
                    </li>

                    <li class="nav-item">
                        <a use:link class="nav-link" href="/pet-culture-center">강남구 문화시설</a>
                    </li>
                {/if}
            </ul>
        </div>
    </div>
</nav>