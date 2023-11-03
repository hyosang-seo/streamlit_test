import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import ssl
ssl._create_default_https_context = ssl._create_unverified_context 
# Streamlit 페이지 너비 조정
st.set_page_config(
    page_title="Streamlit에서 Pygwalker 사용",
    layout="wide"
)
 
# 제목 추가
st.title("Streamlit에서 Pygwalker 사용하기")
 
# 데이터 가져오기
df = pd.read_csv("./bike_sharing_dc.csv")
 
# Pygwalker를 사용하여 HTML 생성

vis_spec = r"""{"config":"[{\"visId\":\"gw_Q1a1\",\"name\":\"Chart 1\",\"encodings\":{\"dimensions\":[{\"dragId\":\"gw_lZwL\",\"fid\":\"GW_134F5I1A28\",\"name\":\"date\",\"basename\":\"date\",\"semanticType\":\"temporal\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_Lz5C\",\"fid\":\"GW_8FAUTAFA52O\",\"name\":\"month\",\"basename\":\"month\",\"semanticType\":\"ordinal\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_bq3H\",\"fid\":\"GW_1R6AE0LVJFSXC\",\"name\":\"season\",\"basename\":\"season\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_H6We\",\"fid\":\"GW_1BBA6IQGC0\",\"name\":\"year\",\"basename\":\"year\",\"semanticType\":\"ordinal\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_T314\",\"fid\":\"GW_BAKKITGENAYDKG\",\"name\":\"holiday\",\"basename\":\"holiday\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_edAJ\",\"fid\":\"GW_1EA5218PV0Y1MYYOHRFD0CCI3OW\",\"name\":\"work yes or not\",\"basename\":\"work yes or not\",\"semanticType\":\"ordinal\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_oOWe\",\"fid\":\"GW_22X4ZRCC5O4FUDKG\",\"name\":\"am or pm\",\"basename\":\"am or pm\",\"semanticType\":\"nominal\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_UKmS\",\"fid\":\"GW_SSD6TPW7PF6GR99V6OH441C6Y8\",\"name\":\"Day of the week\",\"basename\":\"Day of the week\",\"semanticType\":\"quantitative\",\"analyticType\":\"dimension\"},{\"dragId\":\"gw_mea_key_fid\",\"fid\":\"gw_mea_key_fid\",\"name\":\"Measure names\",\"analyticType\":\"dimension\",\"semanticType\":\"nominal\"}],\"measures\":[{\"dragId\":\"gw_VgD7\",\"fid\":\"GW_14PB7VG374\",\"name\":\"hour\",\"basename\":\"hour\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_o5XH\",\"fid\":\"GW_OU2NNYUF526UM4N5T4XC\",\"name\":\"temperature\",\"basename\":\"temperature\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_zBSE\",\"fid\":\"GW_4BD4VXTFLWPCBNU3CP604W\",\"name\":\"feeling_temp\",\"basename\":\"feeling_temp\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_RLdI\",\"fid\":\"GW_28BTNDV55877F2UO\",\"name\":\"humidity\",\"basename\":\"humidity\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_Jo40\",\"fid\":\"GW_2JTS921YL9JS5B1S\",\"name\":\"winspeed\",\"basename\":\"winspeed\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_yz8j\",\"fid\":\"GW_1IENDDF0AB38W\",\"name\":\"casual\",\"basename\":\"casual\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_gxNM\",\"fid\":\"GW_3FKGZOVLAUQ2KI1LPV4\",\"name\":\"registered\",\"basename\":\"registered\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw__VUY\",\"fid\":\"GW_7NL4CV2YF5C\",\"name\":\"count\",\"basename\":\"count\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"},{\"dragId\":\"gw_count_fid\",\"fid\":\"gw_count_fid\",\"name\":\"Row count\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\",\"computed\":true,\"expression\":{\"op\":\"one\",\"params\":[],\"as\":\"gw_count_fid\"}},{\"dragId\":\"gw_mea_val_fid\",\"fid\":\"gw_mea_val_fid\",\"name\":\"Measure values\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"}],\"rows\":[{\"dragId\":\"gw_FORa\",\"fid\":\"GW_7NL4CV2YF5C\",\"name\":\"count\",\"basename\":\"count\",\"analyticType\":\"measure\",\"semanticType\":\"quantitative\",\"aggName\":\"sum\"}],\"columns\":[{\"dragId\":\"gw_VFLX\",\"fid\":\"GW_134F5I1A28\",\"name\":\"date\",\"basename\":\"date\",\"semanticType\":\"temporal\",\"analyticType\":\"dimension\"}],\"color\":[],\"opacity\":[],\"size\":[],\"shape\":[],\"radius\":[],\"theta\":[],\"longitude\":[],\"latitude\":[],\"geoId\":[],\"details\":[],\"filters\":[],\"text\":[]},\"config\":{\"defaultAggregated\":true,\"geoms\":[\"auto\"],\"showTableSummary\":false,\"coordSystem\":\"generic\",\"stack\":\"stack\",\"showActions\":false,\"interactiveScale\":false,\"sorted\":\"none\",\"zeroScale\":true,\"scaleIncludeUnmatchedChoropleth\":false,\"size\":{\"mode\":\"fixed\",\"width\":635,\"height\":502},\"format\":{},\"geoKey\":\"name\",\"resolve\":{\"x\":false,\"y\":false,\"color\":false,\"opacity\":false,\"shape\":false,\"size\":false},\"limit\":-1}}]","chart_map":{},"version":"0.3.9"}"""

walker = pyg.walk(df, spec=vis_spec)
pyg_html = walker.to_html()

# Streamlit 앱에 HTML 포함
components.html(pyg_html, height=1000, scrolling=True)
