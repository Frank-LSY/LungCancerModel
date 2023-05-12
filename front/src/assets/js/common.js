import { useToast } from "vue-toastification";

const toast = useToast()

const options = {
    timeout: 1500,
    position: "top-center",
    hideProgressBar: true,
    closeButton: false
}

const successMessage = (msg) => {
    toast.success(msg, options)
}

const warningMessage = (msg) => {
    toast.warning(msg, options)
}

const infoMessage = (msg) => {
    toast.info(msg, options)
}

const errorMessage = (msg) => {
    toast.error(msg, options)
}

export { successMessage, warningMessage, infoMessage, errorMessage }