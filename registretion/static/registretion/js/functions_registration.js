function printError(error,form){
    Object.keys(error).forEach(errorKey=>{
        const p=document.createElement("p")
        if (!(form.elements[errorKey].nextElementSibling instanceof HTMLParagraphElement)){
            p.classList.add("error");
            p.textContent=error[errorKey];
            form.elements[errorKey].after(p);
            form.elements[errorKey].classList.add("error-field")
        }
        const call=e=>{
            p.remove();
            form.elements[errorKey].classList.remove("error-field")
            form.elements[errorKey].removeEventListener("click",call)
        }
        
        form.elements[errorKey].addEventListener("click",call)
    })
}