export function run(){
    console.log("App is running")
    return ()=>{
        console.log("App is stopping")
    }
}