# -*- coding:utf-8 -*-
import re
import urlparse
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容，抽取url和数据
        :param page_url: 下载页面的url
        :param html_cont: 下载网页的内容
        :return: 返回url和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self,page_url,soup):
        '''
        抽取新的url集合
        :param page_url: 下载页面的url
        :param soup: soup
        :return: 返回新的url集合
        '''
        new_urls=set()
        #抽取符合标记a的标记
        links=soup.find_all('a',href)





