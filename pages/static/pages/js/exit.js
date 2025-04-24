async function exit(path,form,main){
    await sentForm(path,form)
    renderHtml("/registration",main)
}