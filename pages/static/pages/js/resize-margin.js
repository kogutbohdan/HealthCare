function resizeMargintTop(selector,size){
    return ()=>{
        const element=document.querySelector(selector)
        if(element){
            element.style.marginTop=`${element.parentElement.offsetHeight*size}px`       
        }
    }
}

window.addEventListener("resize",resizeMargintTop(".exe-box",0.04))
window.addEventListener("resize",resizeMargintTop("header",0.12))
window.addEventListener("resize",resizeMargintTop(".top-box",0.04))