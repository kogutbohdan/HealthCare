async function removeForm(path, form, callback) {
    const result = await sentForm(path, form)
    if (result.status == "ok") {
        callback(result)
    }
}

const buyIcon = (path, form) => {
    removeForm(path, form, (result) => {
        form.remove()
        const coinCounter = document.querySelector("#many-print")
        coinCounter.textContent = result["many"]
    })
}

const saveTask = async (path, form, main) => {
    if (await submit(path, form, main)){
        //form.parentElement.remove()
    }
}