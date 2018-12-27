<template>
    <div id="app"> 
        <div id="header">
            <img src="./components/b.png">
        </div>
        <RandomNumInput></RandomNumInput>
        <RandomNumResult></RandomNumResult>
      
        <div class="type1">Link</div>
        <p><a href="ec2-13-124-15-96.ap-northeast-2.compute.amazonaws.com:8080">▶ Blockchain Composer</a></p>
        <p><a href="ec2-13-124-15-96.ap-northeast-2.compute.amazonaws.com:3000">▶ Blockchain Rest server</a></p>
        <div id="footer">
        </div>
    </div>

</template>
<script type="text/javascript">
import RandomNumInput from './components/RandomNumInput.vue';
import RandomNumResult from './components/RandomNumResult.vue';

export default {
    name : 'app',
    components : {RandomNumInput, RandomNumResult}
    
}
</script>

<!--<style lang="scss" scoped>
@import "../../scss/style";
</style>-->