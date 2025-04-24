async function buyIcon(path,form){
    const result=await sentForm(path,form)
    if(result.status=="ok"){
        form.remove()
        const coinCounter=document.querySelector("#many-print")
        console.log(coinCounter)
        coinCounter.textContent=result["many"]
    }
}