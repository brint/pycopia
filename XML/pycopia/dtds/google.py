#!/usr/bin/python

# This file generated by a program. do not edit.


import pycopia.XML.POM

class Gsp(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('VER', 1, 11, None), 
         ])
	_name = u'GSP'


class Error(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'ERROR'


class Tm(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'TM'


class Q(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'Q'


class Cache(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CACHE'


class Cache_url(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CACHE_URL'


class Cache_redir_url(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CACHE_REDIR_URL'


class Cache_last_modified(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CACHE_LAST_MODIFIED'


class Cache_legend_found(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CACHE_LEGEND_FOUND'


class Cache_legend_text(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('fgcolor', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('bgcolor', 1, 11, None), 
         ])
	_name = u'CACHE_LEGEND_TEXT'


class Cache_legend_notfound(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CACHE_LEGEND_NOTFOUND'


class Cache_content_type(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CACHE_CONTENT_TYPE'


class Cache_language(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CACHE_LANGUAGE'


class Cache_encoding(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CACHE_ENCODING'


class Cache_html(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CACHE_HTML'


class Blob(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('encoding', 1, 11, None), 
         ])
	_name = u'BLOB'


class Param(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('original_value', 1, 11, None), 
         ])
	_name = u'PARAM'


class Cb(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 1, 11, None), 
         ])
	_name = u'CB'


class Cs(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 1, 11, None), 
         ])
	_name = u'CS'


class Ct(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CT'


class Tt(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'TT'


class Gm(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'GM'


class Gl(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'GL'


class Gd(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'GD'


class Isurl(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	_name = u'ISURL'


class Rpb(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	_name = u'RPB'


class Bpb(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	_name = u'BPB'


class Spelling(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'Spelling'


class Suggestion(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('q', 1, 11, None), 
         ])
	_name = u'Suggestion'


class Calc(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CALC'


class Rhs(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'RHS'


class Lhs(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LHS'


class Relatedsearches(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'RelatedSearches'


class Relatedsearch(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'RelatedSearch'


class Synonyms(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'Synonyms'


class Onesynonym(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('q', 1, 11, None), 
         ])
	_name = u'OneSynonym'


class News(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'NEWS'


class Source(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'SOURCE'


class Date(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DATE'


class Maps(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'MAPS'


class Map(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'MAP'


class Dictionary(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DICTIONARY'


class Word(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'WORD'


class Definitions(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DEFINITIONS'


class Definition(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('N', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('MIME', 1, 13, u'text/html'), 
         ])
	_name = u'DEFINITION'


class Definition_term(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DEFINITION_TERM'


class Definition_defn(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DEFINITION_DEFN'


class Definition_language(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DEFINITION_LANGUAGE'


class Definition_extension(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('N', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('MIME', 1, 13, u'text/html'), 
         ])
	_name = u'DEFINITION_EXTENSION'


class Definition_other_language(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('N', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('MIME', 1, 13, u'text/html'), 
         ])
	_name = u'DEFINITION_OTHER_LANGUAGE'


class Local_listings(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LOCAL_LISTINGS'


class Local_listing(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LOCAL_LISTING'


class Prose_results(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PROSE_RESULTS'


class Prose_main(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PROSE_MAIN'


class Prose_addl(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PROSE_ADDL'


class Body_line(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'BODY_LINE'


class Block(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'BLOCK'


class N(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'N'


class Address(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'ADDRESS'


class Phone_number(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PHONE_NUMBER'


class Distance_away(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DISTANCE_AWAY'


class Image_thumbs(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'IMAGE_THUMBS'


class Image_thumb(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'IMAGE_THUMB'


class Image_source(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'IMAGE_SOURCE'


class Image_height(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'IMAGE_HEIGHT'


class Image_width(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'IMAGE_WIDTH'


class Froogle_listings(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'FROOGLE_LISTINGS'


class One_froogle(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'ONE_FROOGLE'


class Price(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PRICE'


class Merchant(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'MERCHANT'


class Scholar_listings(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'SCHOLAR_LISTINGS'


class One_scholar(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'ONE_SCHOLAR'


class Scholar_author(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'SCHOLAR_AUTHOR'


class Scholar_citations(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'SCHOLAR_CITATIONS'


class Print_listings(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PRINT_LISTINGS'


class One_print(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'ONE_PRINT'


class Print_author(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PRINT_AUTHOR'


class Print_pages(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PRINT_PAGES'


class Ads(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'ADS'


class Ad(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('n', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('type', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('url', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('visible_url', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('ctc_url', 1, 13, u''), 
         ])
	_name = u'AD'


class Line1(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LINE1'


class Line2(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LINE2'


class Line3(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LINE3'


class Cpc(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CPC'


class Wcpc(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'WCPC'


class Pcpm(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PCPM'


class Regionname(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'REGIONNAME'


class Commercial(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'COMMERCIAL'


class Res(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('FILTERED', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('SN', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('EN', 1, 11, None), 
         ])
	_name = u'RES'


class M(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'M'


class Fi(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	_name = u'FI'


class Xt(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	_name = u'XT'


class Nb(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'NB'


class Pu(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PU'


class Nu(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'NU'


class R(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('N', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('N1', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('L', 1, 13, u'1'), 
         pycopia.XML.POM.XMLAttribute('MIME', 1, 13, u'text/html'), 
         ])
	_name = u'R'


class U(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'U'


class Ue(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'UE'


class Ut(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'UT'


class Ute(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'UTE'


class Ud(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'UD'


class T(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'T'


class Rk(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'RK'


class Localinfo(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LOCALINFO'


class Localquery(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LOCALQUERY'


class Latlng_param(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LATLNG_PARAM'


class Bn(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'BN'


class Ph(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PH'


class Addr(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'ADDR'


class Citystate(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CITYSTATE'


class Zip(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'ZIP'


class Latitude(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LATITUDE'


class Longitude(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LONGITUDE'


class Radius(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'RADIUS'


class Crawldate(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CRAWLDATE'


class Xp(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'XP'


class Fs(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('NAME', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('VALUE', 1, 11, None), 
         ])
	_name = u'FS'


class F(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'F'


class S(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'S'


class Lang(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'LANG'


class Has(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'HAS'


class Debug(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DEBUG'


class Ind_debug(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'IND_DEBUG'


class Doc_debug(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DOC_DEBUG'


class Di(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DI'


class Cat(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('SE', 1, 13, u'ISO-8859-1'), 
         ])
	_name = u'CAT'


class Gn(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'GN'


class Fvn(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'FVN'


class Dt(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DT'


class Ds(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'DS'


class L(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('TAG', 1, 13, u'link:'), 
         ])
	_name = u'L'


class C(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('TAG', 1, 13, u'cache:'), 
         pycopia.XML.POM.XMLAttribute('SZ', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('ENC', 1, 13, u''), 
         pycopia.XML.POM.XMLAttribute('CID', 1, 13, u''), 
         ])
	_name = u'C'


class Rt(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('TAG', 1, 13, u'related:'), 
         ])
	_name = u'RT'


class Pers_cats(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'PERS_CATS'


class Hn(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('U', 1, 11, None), 
         ])
	_name = u'HN'


class Mt(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('N', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('V', 1, 11, None), 
         ])
	_name = u'MT'


class Revs(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('RPOS', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('ODEL', 1, 11, None), 
         ])
	_name = u'REVS'


class Fq(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'FQ'


class Rev(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('N', 1, 12, None), 
         ])
	_name = u'REV'


class Car(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'CAR'


class Md(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('N', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('V', 1, 11, None), 
         ])
	_name = u'MD'


GENERAL_ENTITIES = {}