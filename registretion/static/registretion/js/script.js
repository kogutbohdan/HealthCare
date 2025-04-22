

const main=document.querySelector("main");
const header=document.querySelector("header");
renderHtml("/registration",main);


main.addEventListener("click",e=>{
    if (e.target.href){
        e.preventDefault();
        renderHtml(e.target.href,main);
        console.log(e.target.href);
    }
    console.log(e.target.classList)
        
})


main.addEventListener("submit",e=>{
    e.preventDefault();
    if(e.target.action){
        submits[e.target.action.replace("http://127.0.0.1:8000/","")](e.target.action,e.target,main);
    }
});