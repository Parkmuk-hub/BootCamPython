// 간단한 선택자 함수
const $ = (sel) => document.querySelector(sel);

$("#sendBtn").addEventListener("click", async () => {
    const name = $("#name").value.trim();
    const age = $("#age").value.trim();

    // 1. URLSearchParams를 사용해야 한글 인코딩과 ?name=...&age=... 형식이 올바르게 만들어집니다.
    const params = new URLSearchParams({ name, age });
    const url = `/api/friend?${params.toString()}`;

    $("#result").textContent = "요청중....";

    try {
        const res = await fetch(url, {
            method: "GET",
            headers: { "Accept": "application/json" }
        });

        const data = await res.json();

        if (!res.ok || data.ok === false) {
            $("#result").innerHTML = `<span style="color:red">오류 : ${data.error}</span>`;
            return;
        }

        // 2. 서버에서 받은 데이터를 화면에 표시
        $("#result").innerHTML = `
            <div style="margin-top:20px; border-top:1px solid #ccc; padding-top:10px;">
                <p>이름: ${data.name}</p>
                <p>나이: ${data.age}</p>
                <p>연령대: ${data.age_group}</p>
                <p style="font-weight:bold; color:blue;">메시지: ${data.message}</p>
            </div>
        `;
    } catch (err) {
        $("#result").innerHTML = `<span style="color:red">연결 오류: ${err.message}</span>`;
    }
});