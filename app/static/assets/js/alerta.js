

/** Alerta personalizadas */
function mensajeAlerta(msg, tipo_msg='') {
    let text  = document.querySelector('.text-2').textContent = `${msg}`;

    const toast    = document.querySelector(".toast");
        closeIcon  = document.querySelector(".close"),
        progress   = document.querySelector(".progress");


    toast.classList.add("active");
    progress.classList.add("active");


    setTimeout(() => {
        toast.classList.remove("active");
    }, 5000);

    closeIcon.addEventListener("click", () => {
        toast.classList.remove("active");
    });
}

//Create sweet alert with error message for delete action
function deleteAlert() {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 2500,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer);
            toast.addEventListener('mouseleave', Swal.resumeTimer);
        }
    });

    Toast.fire({
        icon: "error",
        title: "No se puede eliminar este registro. La ruta de la foto es incorrecta"
    });
}

/**Ocultando la alerta que se dispara sin el JavaScript */
let verificar_clase = $(".mi_alerta").hasClass("active")
console.log(verificar_clase);
if(verificar_clase ==true){
    setTimeout(() => {
        $(".mi_alerta").removeClass("active");
    }, 5000);
}