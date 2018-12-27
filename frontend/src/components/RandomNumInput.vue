<!--난수생성 정보입력 Vue-->
<template>
    <div>
        <h4>생성조건 </h4><br>
        고객사 :
        <select v-model.trim="company" >
            <option value="L_BLACKYARK">블랙야크</option>
            <option value="B_BRANDSAFER">브랜드세이퍼</option>
            <option value="C_COSTORY">파파레서피</option>
            <option value="G_JAYJUN">제이준메딕스㈜</option>
            <option value="D_ISID">아이시드</option>
            <option value="M_MUNMU">TWOTSP</option>
            <option value="X_HUXLEY">(주)노드메이슨</option>
            <option value="U_JAYJUN2">제이준코스메틱㈜</option>
            <option value="P_MUNKYUNG">문경오미자</option>
            <option value="4_VERFLOS">오감 바이오</option>
        </select>&nbsp;&nbsp; 난수 표현식 :
        <select v-model.trim="regex">
            <option disabled value="">표현식</option>
            <option value="[\w\d]{15}_1">1</option>
            <option value="[\w\d]{15}_2">2</option>
            <option value="[\w\d]{15}_3">3</option>
        </select> &nbsp;&nbsp; 발권 개수 :
        <input size="1px" type="text" id="number" v-model.trim="number" />
        파일 라인 수 :
        <input size="1px" type="text" id="fileline" v-model.trim="fileline" />
        <div class="button">
            <div class="eff"></div>
            <a href="#" v-on:click="send"> 생성하기 </a>
        </div>      
    </div>
</template>
<script type="text/javascript">
import eventBus from '../EventBus'
import axios from 'axios'
export default {
    name: 'input-component',
    data: function() {
        return {
            da:"",
            company: "",
            regex: "",
            number: 0,
            fileline: 0,
            zipfilename: ""
            /*
            formData = new FormData(),
            imagefile = document.querySelector('#file')
            */
        }
    },
    methods: {
        /*
        생성조건에서 선택한 value들을 서버로 보냄
        axios.post('url',data,config)
        */
        send: function() {
            const path = 'http://127.0.0.1:5000/api/random'
            axios.post(path, {'company': this.company, 'regex':this.regex, 'number':this.number, 'fileline':this.fileline})
             .then(response => {
                console.log(response)
                this.outputNumber = response.data.number
                this.company = response.data.company
                this.regex = response.data.regex
                this.number = response.data.number
                this.zipfilename = response.data.zipfilename
                eventBus.$emit('sendFilename', this.zipfilename)
            })
            .catch(error => {
                console.log(error)
            })

        },
    }
}
</script>

<!--<style lang="scss" scoped>
@import "../../scss/style";
</style>-->

<style>
body {
    background: #F6F6F6;
    width: auto;
    position: relative;
    object-fit: contain;
    display: table;
    margin: auto;
}

.container {
    height: 100%;
    display: table-cell;
    vertical-align: middle;
}

.main {
    height: 200px;
    width: 200px;
    background-color: blue;
}

#header {
    background: #34495e;
    height: 75px;
}

#sidebar {
    background: #F6F6F6;
    float: left;
    width: 100px;
    height: 600px;
}

h4,
div>h4 {
    background: white;
    line-height: 40px
}

select {
    width: 200px;
    /* 원하는 너비설정 */
    padding: .8em .5em;
    /* 여백으로 높이 설정 */
    font-family: inherit;
    /* 폰트 상속 */
    background: url(https://farm1.staticflickr.com/379/19928272501_4ef877c265_t.jpg) no-repeat 95% 50%;
    /* 네이티브 화살표 대체 */
    border: 1px solid #999;
    border-radius: 0px;
    /* iOS 둥근모서리 제거 */
    -webkit-appearance: none;
    /* 네이티브 외형 감추기 */
    -moz-appearance: none;
    appearance: none;
}

input {
    width: 50px;
    background-color: #F6F6F6;
    /* 여백으로 높이 설정 */
    padding: .8em .5em;
    /* iOS 둥근모서리 제거 */
    border: 1px solid #999;
    border-radius: 0px;
}


/*버튼 CSS*/

.button {
    width: 140px;
    height: 50px;
    border: 2px solid #34495e;
    float: right;
    text-align: center;
    cursor: pointer;
    position: relative;
    box-sizing: border-box;
    overflow: hidden;
    margin: 0 0 40px 50px;
}

.button a {
    font-family: arial;
    font-size: 16px;
    color: #fff;
    text-decoration: none;
    line-height: 50px;
    position: relative;
    transition: all .5s ease;
    z-index: 2;
}

.eff {
    width: 140px;
    height: 50px;
    border: 70px solid #34495e;
    transition: all .5s ease;
    position: absolute;
    z-index: 1;
    box-sizing: border-box;
}

.button:hover .eff {
    border: 0px solid #34495e;
}

.button:hover a {
    color: #34495e;
}

div.type1 {
    padding: 10px;
    font-weight: bold;
    vertical-align: top;
    color: #fff;
    background: #34495e;
    margin: 20px 0px;
}


/*링크*/

/* a:visited {
    text-decoration: none;
    color: #333조333;
}*/

a:link {
    text-decoration: none;
    /* color: white;*/
}

a:active {
    text-decoration: none;
    color: #333333;
}

a:hover {
    text-decoration: none;
    color: rgb(10, 9, 9);
}


/**/

ol {
    counter-reset: li;
    /* Initiate a counter */
    margin-left: 0;
    /* Remove the default left margin */
    padding-left: 0;
    /* Remove the default left padding */
}

ol>li:before {
    /* Use the counter as content */
    counter-increment: li;
    /* Increment the counter by 1 */
    /* Position and style the number */
    position: absolute;
    top: -2px;
    left: -2em;
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    width: 2em;
    /* Some space between the number and the content in browsers that support
generated content but not positioning it (Camino 2 is one example) */
    margin-right: 8px;
    padding: 4px;
    border-top: 2px solid #666;
    color: #fff;
    background: #666;
    font-weight: bold;
    font-family: "Helvetica Neue", Arial, sans-serif;
    text-align: center;
}

ol {
    list-style: none;
}

li ol,
li ul {
    margin-top: 6px;
}

ol ol li:last-child {
    margin-bottom: 0;
}

.rectangle-list a {
    position: relative;
    display: block;
    padding: .4em .4em .4em .8em;
    *padding: .4em;
    margin: .5em 0 .5em 2.5em;
    background: #ddd;
    color: #444;
    text-decoration: none;
    transition: all .3s ease-out;
}

.rectangle-list a:hover {
    background: #eee;
}

.rectangle-list a:before {
    content: counter(li);
    counter-increment: li;
    position: absolute;
    left: -2.5em;
    top: 50%;
    margin-top: -1em;
    background: #7b72fa;
    height: 2em;
    width: 2em;
    line-height: 2em;
    text-align: center;
    font-weight: bold;
}

.rectangle-list a:after {
    position: absolute;
    content: '';
    border: .5em solid transparent;
    left: -1em;
    top: 50%;
    margin-top: -.5em;
    transition: all .3s ease-out;
}

.rectangle-list a:hover:after {
    left: -.5em;
    border-left-color: #7b72fa;
}

#list {
    width: 600px;
    border: 1px solid black;
    border-collapse: collapse;
}

#list td,
#list th {
    border: 1px solid black;
    text-align: center;
}

#list>thead>tr {
    color: yellow;
    background-color: purple;
}

[v-cloak] {
    display: none;
}
</style>