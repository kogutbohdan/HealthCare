

const main=document.querySelector("main");
const header=document.querySelector("header");
renderHtml("/registration",main);


main.addEventListener("click",e=>{
    if (e.target.href){
        e.preventDefault();
        renderHtml(e.target.href,main);
        console.log(e.target.href);
    }
})


main.addEventListener("submit",e=>{
    e.preventDefault();
    const func=e.target.dataset.function
    if(e.target.action){
        submit(e.target.action,e.target,main);
        e.target.reset();
    }
});