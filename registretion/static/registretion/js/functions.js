async function renderHtml(url,main){
    const result=await fetch(url,{
        headers:{
            "X-Requested-With":"XMLHttpRequest"
        },
    })
    const html=await result.text();
    main.innerHTML=html;
}

function getToken(form){
    return form.querySelector("[name=csrfmiddlewaretoken]").value;
}