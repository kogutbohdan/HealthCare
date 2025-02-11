const forms_conteiner=document.querySelectorAll("section")

document.querySelector("nav").addEventListener("click",e=>{
    e.preventDefault();
    if (e.target.textContent=="Регістрація"){
        forms_conteiner[0].classList.add("activation")
        forms_conteiner[1].classList.remove("activation")
    }else if (e.target.textContent=="Авторизація"){
        forms_conteiner[1].classList.add("activation")
        forms_conteiner[0].classList.remove("activation")
    }
})