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

async function sentForm(path,form){
    const formData = new FormData(form);
        const response = await fetch(path, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getToken(form),
            },
            credentials: 'same-origin',  // include credentials to send cookies to the server
            body: formData,
        });
        return await response.json();
}

function handleJsonResponse(json, main, form) {
    if (json["page"]) {
        renderHtml(json["page"], main);
        return
        
    } else if (json["errors"]) {
        printError(json["errors"], form);
    }
}

const submit=async (path,form,main) => {
    const json=await sentForm(path,form)
    handleJsonResponse(json, main, form)
    form.reset();
}
