<template>
    <div>

        <button type="button" class="btn btn-primary">{{ msg }}</button>

    </div>
</template>

<script>
import axios from 'axios'
export default {

    name: 'shark-component',
    data() {
        return {
            msg : "Hello, this is Shark "
        }
    },
    methods : {
        getResponse () {
            const path = 'http://localhost:5000/shark'
            axios.get(path)
            .then ((resp) => {
                console.log(resp.data)
                this.msg = resp.data
            })
            .catch( (err) => {
                console.error(err)
            })
        }   
    },
    created(){
        this.getResponse()
    }
}

</script>