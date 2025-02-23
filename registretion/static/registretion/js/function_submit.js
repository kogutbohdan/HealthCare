const functionsSubmit={
    registration:async (form,main)=>{

        const formData = new FormData(form);
        const response = await fetch('save_user_bd/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getToken(form),
            },
            credentials: 'same-origin',  // include credentials to send cookies to the server
            body: formData,
        });
        const json = await response.json();
        if (json["page"]){
            renderHtml(json["page"],main);
        }
        console.log(json);
    }
}
