async function changePassword(path,form,main){
    const result=await sentForm(path,form)
    handleJsonResponse(result, main, form)
    form.reset()
}