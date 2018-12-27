<!--난수생성 history와 난수생성 csv파일 다운로드 Vue-->
<template >
<div>
    <br/>
        <h4>생성결과 </h4>
        <div class="type1">생성코드 목록</div>
    <v-flex class="app1">
        <v-text-field color="#7b72fa" class="search" label="Search Company..."
                    v-model="search">
        </v-text-field>
      <v-list class="v_app" v-for="(listData, index) in calData" :key="index">
        <ol id="result" class="rectangle-list">
            <li><a href="#">{{listData.id}}. {{listData.subject}} - {{listData.desc}}</a></li>
        </ol>
      </v-list>
      <br><br>
      <div class="paginate"> 
      <v-pagination 
        v-model="curPageNum"
        :length="numOfPages"
         color="#666">
      </v-pagination>
      </div>
    </v-flex>
    <div class="type1">결과</div>
    <!-- <pre>{{ result|tojson_pretty|safe }}</pre> -->
    <p><a href="" @click="getfile"><h4>{{zipfilename}}</h4></a></p>
</div>
</template>
<script type="text/javascript">
import eventBus from '../EventBus'
import axios from 'axios'
const testData = [{"id": 1,"subject": "Malawi","desc": "Wels"},{"id": 2,"subject": "Cuba","desc": "Sale"},{"id": 3,"subject": "Somalia","desc": "Lahore"},{"id": 4,"subject": "Togo","desc": "Termeno sulla strada del vino/Tramin an der Weinstrasse"},{"id": 5,"subject": "Slovenia","desc": "Edam"},{"id": 6,"subject": "Tonga","desc": "Vinci"},{"id": 7,"subject": "Kenya","desc": "Te Awamutu"},{"id": 8,"subject": "Japan","desc": "Ferrazzano"},{"id": 9,"subject": "Finland","desc": "Nil-Saint-Vincent-Saint-Martin"},{"id": 10,"subject": "Dominica","desc": "Paglieta"},{"id": 11,"subject": "Solomon Islands","desc": "Vilvoorde"},{"id": 12,"subject": "Monaco","desc": "Tonk"},{"id": 13,"subject": "Cook Islands","desc": "Sint-Pieters-Kapelle"},{"id": 14,"subject": "Gibraltar","desc": "Develi"},{"id": 15,"subject": "Mauritania","desc": "Etobicoke"},{"id": 16,"subject": "Sierra Leone","desc": "Norman Wells"},{"id": 17,"subject": "Ghana","desc": "Charleroi"},{"id": 18,"subject": "Saint Martin","desc": "Düsseldorf"},{"id": 19,"subject": "Uganda","desc": "Dhuy"},{"id": 20,"subject": "Serbia","desc": "Rampur"},{"id": 21,"subject": "Bangladesh","desc": "Kempten"},{"id": 22,"subject": "Bosnia and Herzegovina","desc": "Okigwe"},{"id": 23,"subject": "Somalia","desc": "Valpelline"},{"id": 24,"subject": "Libya","desc": "Beverlo"},{"id": 25,"subject": "Israel","desc": "Coalhurst"},{"id": 26,"subject": "Greece","desc": "Castel Ritaldi"},{"id": 27,"subject": "United Kingdom (Great Britain)","desc": "Benestare"},{"id": 28,"subject": "Singapore","desc": "Tsiigehtchic"},{"id": 29,"subject": "Saint Pierre and Miquelon","desc": "Jhang"},{"id": 30,"subject": "South Georgia and The South Sandwich Islands","desc": "Mobile"},{"id": 31,"subject": "Yemen","desc": "Koningshooikt"},{"id": 32,"subject": "Albania","desc": "Stirling"},{"id": 33,"subject": "Laos","desc": "Beypazarı"},{"id": 34,"subject": "Bouvet Island","desc": "Florida"},{"id": 35,"subject": "Macao","desc": "Calmar"},{"id": 36,"subject": "Austria","desc": "Invergordon"},{"id": 37,"subject": "Palau","desc": "Balclutha"},{"id": 38,"subject": "Denmark","desc": "Bozeman"},{"id": 39,"subject": "Sierra Leone","desc": "Assiniboia"},{"id": 40,"subject": "Austria","desc": "Champigny-sur-Marne"},{"id": 41,"subject": "Finland","desc": "Calera de Tango"},{"id": 42,"subject": "Lesotho","desc": "Ancarano"},{"id": 43,"subject": "Western Sahara","desc": "Cochamó"},{"id": 44,"subject": "Guernsey","desc": "Villers-lez-Heest"},{"id": 45,"subject": "Turkey","desc": "Liedekerke"},{"id": 46,"subject": "Dominica","desc": "Nanterre"},{"id": 47,"subject": "Saint Helena, Ascension and Tristan da Cunha","desc": "Crato"},{"id": 48,"subject": "Czech Republic","desc": "Lossiemouth"},{"id": 49,"subject": "Croatia","desc": "Sale"},{"id": 50,"subject": "South Georgia and The South Sandwich Islands","desc": "North Shore"},{"id": 51,"subject": "Malawi","desc": "Newtonmore"},{"id": 52,"subject": "Marshall Islands","desc": "Piracicaba"},{"id": 53,"subject": "Nepal","desc": "Ponoka"},{"id": 54,"subject": "Gibraltar","desc": "Rabbi"},{"id": 55,"subject": "Åland Islands","desc": "Biarritz"},{"id": 56,"subject": "Nepal","desc": "Sant'Elia a Pianisi"},{"id": 57,"subject": "Virgin Islands, British","desc": "Welland"},{"id": 58,"subject": "Nauru","desc": "Sesto al Reghena"},{"id": 59,"subject": "Antarctica","desc": "Eluru"},{"id": 60,"subject": "Seychelles","desc": "San Francisco"},{"id": 61,"subject": "Thailand","desc": "Mango"},{"id": 62,"subject": "Gambia","desc": "Santa Cruz"},{"id": 63,"subject": "Svalbard and Jan Mayen Islands","desc": "Sant'Angelo a Cupolo"},{"id": 64,"subject": "Honduras","desc": "Villata"},{"id": 65,"subject": "Mexico","desc": "Sadiqabad"},{"id": 66,"subject": "Holy See (Vatican City State)","desc": "Villenave-d'Ornon"},{"id": 67,"subject": "Colombia","desc": "Charlottetown"},{"id": 68,"subject": "South Africa","desc": "Latronico"},{"id": 69,"subject": "Korea, South","desc": "Alajuela"},{"id": 70,"subject": "Cambodia","desc": "Montbéliard"},{"id": 71,"subject": "Palau","desc": "Purmerend"},{"id": 72,"subject": "Uzbekistan","desc": "Norrköping"},{"id": 73,"subject": "Rwanda","desc": "Serramonacesca"},{"id": 74,"subject": "Cayman Islands","desc": "Court-Saint-Etienne"},{"id": 75,"subject": "Algeria","desc": "Gonnosfanadiga"},{"id": 76,"subject": "Samoa","desc": "Banff"},{"id": 77,"subject": "Libya","desc": "Amberloup"},{"id": 78,"subject": "Mayotte","desc": "Merchtem"},{"id": 79,"subject": "Bahamas","desc": "Tuscaloosa"},{"id": 80,"subject": "Tunisia","desc": "Fogo"},{"id": 81,"subject": "Liberia","desc": "Launceston"},{"id": 82,"subject": "Guam","desc": "Glendale"},{"id": 83,"subject": "Georgia","desc": "Port Blair"},{"id": 84,"subject": "Isle of Man","desc": "Trochu"},{"id": 85,"subject": "Cook Islands","desc": "Lawton"},{"id": 86,"subject": "Israel","desc": "Istres"},{"id": 87,"subject": "Guam","desc": "Portland"},{"id": 88,"subject": "Brazil","desc": "Barrhead"},{"id": 89,"subject": "Japan","desc": "Walhain"},{"id": 90,"subject": "Bolivia","desc": "Motherwell"},{"id": 91,"subject": "French Polynesia","desc": "Stroud"},{"id": 92,"subject": "Portugal","desc": "Airdrie"},{"id": 93,"subject": "Guinea-Bissau","desc": "Multan"},{"id": 94,"subject": "Bosnia and Herzegovina","desc": "Challand-Saint-Victor"},{"id": 95,"subject": "Reunion","desc": "Moncton"},{"id": 96,"subject": "Bhutan","desc": "Merthyr Tydfil"},{"id": 97,"subject": "Greece","desc": "Rockford"},{"id": 98,"subject": "Swaziland","desc": "San Nicolás"},{"id": 99,"subject": "Antigua and Barbuda","desc": "Rio Grande"},{"id": 100,"subject": "Portugal","desc": "Aalbeke"}]
export default {
    name: 'list-component',
    created : function() {
        /*axios 서버 연결 후 코드
        this.axios.get('url')
        .then((response)=>{
            this.listData = response.data;
        })
        */
        this.listData = testData
        eventBus.$on('sendFilename', this.file);
    },
    data : function() {
        return {
            search: "",
            searchData: [],
            listData: [],
            dataPerPage:10,
            curPageNum:1,
            zipfilename: 'Not Found Download FIle...',
        }
    },
    methods: {
        file : function(zipfilename) {
            if(zipfilename !== ""){
                this.zipfilename = zipfilename;
            }
        },
        // getfile() {
        //   const path = 'http://127.0.0.1:5000/api/files/'
        //     axios.get(path,{responseType: 'blob',})
        //     //axios.responseType = 'blob'
        //     .then((response) => { 
        //         console.log(response)
        //         const url = window.URL.createObjectURL(new Blob([response.data]));
        //         console.log(response.data)
        //         console.log(url)
        //         const link = document.createElement('a'); 
        //         console.log(this.zipfilename) 
        //         link.href = url; 
        //         if(this.zipfilename !== "Not Found Download FIle..."){
        //             link.setAttribute('download', this.zipfilename); 
        //             //or any other extension 
        //             document.body.appendChild(link); 
        //             link.click();
        //         }
        //     });
        // }
        getfile() {
          const path = 'http://127.0.0.1:5000/api/files/'
            axios({
                method: 'post',
                url: path,
                responseType: 'blob',
                data: {
                    zipfilename: this.zipfilename
                }  
            })
            .then((response) => { 
                console.log(response)
                const url = window.URL.createObjectURL(new Blob([response.data]));
                console.log(response.data)
                console.log(url)
                const link = document.createElement('a'); 
                console.log(this.zipfilename) 
                link.href = url; 
                if(this.zipfilename !== "Not Found Download FIle..."){
                    link.setAttribute('download', this.zipfilename); 
                    //or any other extension 
                    document.body.appendChild(link); 
                    link.click();
                }
            });
        }
    },
    computed: {
       startOffset() {
            return ((this.curPageNum - 1) * this.dataPerPage);
        },
        endOffset() {
            return (this.startOffset + this.dataPerPage);
        },

        numOfPages() {
            return Math.ceil(this.listData.length / this.dataPerPage);
        },
        calData() {
            //return this.listData.slice(this.startOffset, this.endOffset);
            this.searchData = this.listData.filter((data) => {
          return data.subject.toLowerCase().includes(this.search.toLowerCase())
        }).slice(0);
 
        return this.searchData.slice(this.startOffset, this.endOffset)
        } 
    }
   
}
</script>

<!--<style lang="scss" scoped>
@import "../../scss/style";
</style>-->

<style>
.search {
    border-color: white;
    width:20%;
}
.paginate{ display: table; margin: 0 auto; width: 50%;}
a button :hover{ background-color: #666; }
.v_app { margin-bottom: -20px;}
body { background: #F6F6F6; width: auto; position: relative; object-fit: contain; 
        display: table;margin: auto; }
#header { background: #34495e; height: 75px; } 
#sidebar { background: #F6F6F6; float: left; width: 100px; height: 600px; }
#footer { background: white; height: 100px; }
h4, div>h4 { background: white; line-height: 40px }
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

/*생성하기 버튼 CSS*/
.button { width: 140px; height: 50px; border: 2px solid #34495e; float: right; text-align: center;
        cursor: pointer; position: relative; box-sizing: border-box; overflow: hidden; margin: 0 0 40px 50px; }
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
.button.eff {
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
p a:visited{
    text-decoration: none;
    color: #040607;
}
p a:link{
    text-decoration: none;
    color: #040607;
}
p a:hover {
    text-decoration: none;
    color: rgb(206, 74, 74);
}

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
    content: /*counter(2)*/'';
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

[v-cloak] {
    display: none;
}
</style>