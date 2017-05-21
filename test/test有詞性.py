from unittest.case import TestCase

from crawler import Spider
from scrapy.selector import Selector
import scrapy


class 有詞性試驗(TestCase):

    def setUp(self):
        self.要求 = scrapy.http.Request(
            'http://e-dictionary.apc.gov.tw/ais/Term.htm',
            meta={'詞條名': '詞條名'},
        )

    def test_有詞性(self):
        rr = scrapy.http.TextResponse(
            'http://e-dictionary.apc.gov.tw/ais/Term.htm',
            body=self.有詞性.encode(),
            encoding='utf-8',
            request=self.要求,
        )
        答案 = [
            {
                "pronounce": "http://e-dictionary.apc.gov.tw/MultiMedia/Audio/tay/atu'_{1}_@_1.1.mp3",
                "pos": "詞類：名詞",
                "sentence": "atu' qasa ga, pinyangan maku'.",
                "zh_Hant": "那區塊是我的耕種地。",
                "description": "解釋1：區、塊、筆",
            },
            {
                "pronounce": None,
                "sentence": "mucing sqasa atu' mu kung.",
                "zh_Hant": "我的區塊一直到那裡。",
                "description": "解釋2：區、塊",
            },
        ]
        結果 = Spider().掠詞條(rr)
        self.assertEqual(結果['examples'], 答案)

    有詞性 = '''
    

<div id="oGHC_Deatail">
    <div id="oGHC_FB"></div>
    <div id="oGHC_Term_Area" class="words">
        
        <div id="oGHC_Term" class="term"><span>atu'</span><a class="play" rel="/MultiMedia/Audio/tay/atu'_{1}.mp3" href="javascript:void(0);"><img title="播放詞項" class="img_audio" src="/images/speaker.gif" alt="播放詞項" style="border-width:0px;" /></a></div>
        
        <div id="oGHC_Freq" class="freq">詞頻：<span class="term_freq">★★ </span>(14)</div>
        <div id="oGHC_Source" class="source">詞根　/　<a href="javascript:void(0)" class="troot" rel="atu'">詞根結構▼</a></div>
    </div>
    <hr class="spline" />
    <div class="e_con">
        
        <div class="concon">
            
            <div class="block"><div><strong>解釋1</strong>：區、塊、筆</div><div class="word_detail"><table class="tb06"><tr><td>詞類：名詞</td></tr></table><table class="tb06"><tr class="st"><td><a href="javascript:void(0)" title="1.區、塊,2.區、塊、筆" rel="260688" class="dsl_term">atu'</a> <a href="javascript:void(0)" title="1.那個" rel="261905" class="dsl_term">qasa</a> <a href="javascript:void(0)" title="1.〔主題標記〕,2.〔語尾助詞〕" rel="260944,260945" class="dsl_term">ga</a>, pinyangan <a href="javascript:void(0)" title="1.我的" rel="261566" class="dsl_term">maku'</a>. <a class="play" rel="/MultiMedia/Audio/tay/atu'_{1}_@_1.1.mp3" href="javascript:void(0);"><img title="播放例句" class="img_audio" src="/images/speaker.gif" alt="播放例句" style="border-width:0px;" /></a></td></tr><tr><td>那區塊是我的耕種地。</td></tr></table></div></div><div class="block"><div><strong>解釋2</strong>：區、塊</div><div class="word_detail"><table class="tb06"><tr class="st"><td><a href="javascript:void(0)" title="1.結尾、結束" rel="265108" class="dsl_term">mucing</a> <a href="javascript:void(0)" title="1.那兒" rel="262160" class="dsl_term">sqasa</a> <a href="javascript:void(0)" title="1.區、塊,2.區、塊、筆" rel="260688" class="dsl_term">atu'</a> <a href="javascript:void(0)" title="1.我的" rel="261575" class="dsl_term">mu</a> kung. </td></tr><tr><td>我的區塊一直到那裡。</td></tr></table></div></div>
            
            
            
            
            
            
            
            
            
            <div id="oGHC_Opinion" class="op260688"></div>
        </div>
        
        <div class="history">
            
            <div id="oGHC_Image" class="pic"></div>
            <div id="oGHC_History" class="hislist"><table class="tbhis"><th>瀏覽歷程</th><tr><td><a href="javascript:void(0)" rel="260688" class="his_term">atu'</td></tr><tr><td><a href="javascript:void(0)" rel="260655" class="his_term">abas</td></tr></table></div>
        </div>
        
    </div>
</div>
<div id="oGHC_PopWin" class="pop_up"></div>
<div id="oGHC_TermsTree" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="260688" title="1.區、塊,2.區、塊、筆">atu'</a>　<ul></li></ul></div>
<div id="oGHC_TermsTreeDE" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="260688">atu'</a>　1.區、塊,2.區、塊、筆<ul></li></ul></div>
<div id="oGHC_TermsTreeSer" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="260688">atu'</a>　1.區、塊,2.區、塊、筆<ul></li></ul></div>
'''
