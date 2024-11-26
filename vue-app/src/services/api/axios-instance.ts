import axios from "axios";

const axiosInstance = axios.create({
    baseURL: "http://0.0.0.0:4000",
    headers: {
        "Content-Type": "application/json"
    }
})


export default axiosInstance



