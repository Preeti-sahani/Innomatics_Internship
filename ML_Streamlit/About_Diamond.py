import streamlit as st

st.set_page_config(page_title="About", page_icon="💎",layout="wide")

st.header('About Diamond')
about= '''
Diamond is a solid form of the element carbon with its atoms arranged in a crystal structure called diamond cubic. 
At room temperature and pressure, another solid form of carbon known as graphite is the chemically stable form of carbon, but diamond converts to it extremely slowly. 
Diamond has the highest hardness and thermal conductivity of any natural material, properties that are used in major industrial applications such as cutting and polishing tools. 
They are also the reason that diamond anvil cells can subject materials to pressures found deep in the Earth.
Because the arrangement of atoms in diamond is extremely rigid, few types of impurity can contaminate it (two exceptions are boron and nitrogen). 
Small numbers of defects or impurities (about one per million of lattice atoms) color diamond blue (boron), yellow (nitrogen), brown (defects), green (radiation exposure), purple, pink, orange, or red. 
Diamond also has a very high refractive index and a relatively high optical dispersion.
'''
st.markdown(about,unsafe_allow_html=True)
col1, col2, col3 = st.columns([3,6,1])
with col1:
    st.write("")
with col2:
    st.image('https://i.imgur.com/Bbf0GWk.jpg')
with col3:
    st.write("")


st.header('Features')
st.image('https://cdn.shopify.com/s/files/1/2292/5973/files/Diamond-4CS-01.jpg?v=1606151870')

st.subheader('Diamond Cut:')
dcut='''
A diamond’s cut refers to how well-proportioned the dimensions of a diamond are, and how these surfaces, or facets, are positioned to create sparkle and brilliance.
A diamond cut is a style or design guide used when shaping a diamond for polishing such as the brilliant cut. Cut does not refer to shape (pear, oval), but the symmetry, proportioning and polish of a diamond. 
The cut of a diamond greatly affects a diamond's brilliance; this means if it is cut poorly, it will be less luminous
'''
st.markdown(dcut,unsafe_allow_html=True)
st.image('http://cilindia.in/wp-content/uploads/2020/09/cut-diamond-uno-comp-horizontal-1024x267.jpg')

st.subheader('Diamond Clarity:')
dclarity='''
 Diamond clarity is a grade on a scale from Flawless to Included, which measures the amount and locations of inclusions in a diamond. 
 An inclusion is an internal or external characteristic or flaw which occurs during the Earth’s natural process of diamond formation. 
 The majority of diamonds contain inclusions that are undetectable to the unaided eye.
'''
st.markdown(dclarity,unsafe_allow_html=True)
st.image('https://static.wixstatic.com/media/c4a033_87424ca6b4964cdd9535e23a266984d0~mv2.jpg/v1/fill/w_889,h_305,al_c/c4a033_87424ca6b4964cdd9535e23a266984d0~mv2.jpg')

st.subheader('Diamond Color:')
dcolor='''
A diamond’s color refers to how clear or yellow it is. 
In general, the highest quality diamonds are totally colorless, whereas lower quality diamonds can often have a slight yellow tint.
'''
st.markdown(dcolor,unsafe_allow_html=True)
st.image('https://qph.cf2.quoracdn.net/main-qimg-976e9eb9b2c7e6c8056d48a217553393-lq')

st.subheader('Diamond Carat:')
dcarat='''
The term ‘carat’ (commonly abbreviated to just ‘ct’) refers to the weight of a diamond, although it is often (incorrectly) used to describe the size of a diamond.
The definition of a carat has changed over time, but since 1913 the international standard has been 200 milligrams, or one-fifth of a gram.
'''
st.markdown(dcarat,unsafe_allow_html=True)
col1, col2, col3 = st.columns([3,6,1])
with col1:
    st.write("")
with col2:
    st.image('https://www.diamondimports.com.au/skin1/images/roundcarat.jpg')
with col3:
    st.write("")
