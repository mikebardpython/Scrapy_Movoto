from http.cookies import SimpleCookie

def cookie_parser():
    cookie_string = '_pxhd=c1868f8e5de995f6c71226d5e2a4c576afbe965c3ef30af3cda2249f27564c01:79afdf21-58eb-11eb-a57f-c7a0d2f75700; RANDOMID=63; _vwo_uuid_v2=DB6C4C0FA9C65120EA3942CDD7462E8BB|de686baa103de561006b199af2122f89; ajs_anonymous_id=%22542fde73-da0f-4328-91b6-8b6b5c882a91%22; _ga=GA1.2.278849678.1610905404; trackingGAID=278849678.1610905404; _pxvid=79afdf21-58eb-11eb-a57f-c7a0d2f75700; pushToken=fHQwc_vx3cDOMtdm4snlh6%3AAPA91bFpug96hz6bp3D4BMJEApFSm_gWI7AvxZNQMKtc5_4cMk_gijq2I-9K6L4fSQCJPJ6XdFMH7tUCuiBBUT71rmiVYgnTp5dMNUoduFQRbUKI3wv2l7Yy8ihcg3sJoQrAOcF0w2zt; LASTMSPVER11=NOVA-TN; _vis_opt_s=1%7C; _vwo_uuid=DED79014B2405BE5731450FC22CEF2E93; _vwo_ds=3%241610918821%3A26.94146087%3A%3A; previousUrl=https%3A%2F%2Fwww.movoto.com%2Ffor-sale%2Fmemphis-tn%2Fsingle-family%2Fprice-0-175000%2Fp-3%2F%4040.9211385%2C-74.1065307%2F; g_state={"i_p":1614135823949,"i_l":4}; LASTSEARCHVIEW=gridView; LASTMSPVER12=VUE-TN; LASTMSPVER13=VUE-TX; _gid=GA1.2.1302872082.1613107153; lastSearchState=TN; SEARCHURL=https%3A%2F%2Fwww.movoto.com%2Ffor-sale%2Fmemphis-tn%2Fsingle-family%2Fprice-0-175000%2F; connect.sid=s%3A_liXQyCIEv2AAMHZHLzqZZC7Nup31e3d.ebQprBsPB6hwSWTeY8wPXDE0TthB9tSTtnaXehxXI5w; _gat=1'
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}

    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    return cookies