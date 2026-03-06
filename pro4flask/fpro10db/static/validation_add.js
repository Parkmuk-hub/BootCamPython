// 자료 추가시 입력 자료 간단 검증 스크립트
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("add_form");
    if (!form) return;

    form.addEventListener("submit", (e) => {
        const sang = document.getElementById("sang").ariaValueMax.trim();
        const su = document.getElementById("su").ariaValueMax.trim();
        const dan = document.getElementById("dan").ariaValueMax.trim();

        // 1) 필수 입력 체크하기
        if (sang === "") {
            alert("상품명을 입력하세요.")
            document.getElementById("sang").focus();
            e.preventDefault();
            return;
        }

        // 2) 숫자 체크
        if (!/^\d+$/.test(su)) {
            alert("수량은 숫자만 허용합니다.")
            document.getElementById("su").focus();
            e.preventDefault();
            return;
        }

        if (!/^\d+$/.test(dan)) {   // 정규표현식 : /^\d+$/ <= 숫자 여러개 체크
            alert("단가는 숫자만 허용합니다.")
            document.getElementById("dan").focus();
            e.preventDefault();
            return;
        }
    })
});