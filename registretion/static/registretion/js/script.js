

const main=document.querySelector("main");
const header=document.querySelector("header");
renderHtml("/registration",main);


main.addEventListener("click",e=>{
    if (e.target.href){
        e.preventDefault();
        renderHtml(e.target.href,main);
        console.log(e.target.href);
    }
    if(e.target.id=="icon"){
        const form = document.querySelector("#icons-form")
        form.classList.add("activate")
    }
    if(e.target.id==="icons-form"){
        e.target.classList.remove("activate")
    }
    if(e.target.parentElement.id==="icons-form"){
        e.target.parentElement.classList.remove("activate")
        e.target.parentElement.previousElementSibling.children[0].src=e.target.src
        e.target.parentElement.children[1].value=e.target.src.replace("http://127.0.0.1:8000/media/","")
        e.target.parentElement.dispatchEvent(new Event('submit',{ bubbles: true, cancelable: true }))
    }
    console.log(e.target.classList)
        
})


main.addEventListener("submit",e=>{
    e.preventDefault();
    if(e.target.action){
        console.log(e.target.action.replace("http://127.0.0.1:8000/","").replace(/\d+/g, ''))
        submits[e.target.action.replace("http://127.0.0.1:8000/","").replace(/\d+/g, '')](e.target.action,e.target,main);
    }
});