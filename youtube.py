import requests
def YOUTUBE(account_id):
    url = f'https://gateway.golike.net/api/advertising/publishers/youtube/jobs?account_id={account_id}'
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3MjE5MjI4NzUsImV4cCI6MTc1MzQ1ODg3NSwibmJmIjoxNzIxOTIyODc1LCJqdGkiOiJEUENZWmFhVXAzZ203TFNmIiwic3ViIjoyMTYyNTU0LCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.cjYFlYRwvs1lbvospy3kGWrUyefNg7av_bGuB_lw8NY',
    'content-type': 'application/json;charset=utf-8',
    'origin': 'https://app.golike.net',
    'priority': 'u=1, i',
    'referer': 'https://app.golike.net/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    't': 'VFZSamVVMTZXVEZOUkVsNFRuYzlQUT09',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    }
    job = requests.get(url,headers=headers).json()
    link = job['data']['link']
    headersYT = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'SAPISIDHASH 1723649281_ede35faf34740e0e3b43082a04c779b73d0650cd',
        'content-type': 'application/json',
        'cookie': 'HSID=A0kaJoJuifOYL_jSb; SSID=AXeVekmMTt9H8z3cq; APISID=enSYyqerMFmfqlOV/AtdYyQJkFh7mli6gB; SAPISID=4vdK4YM32ia-THfm/AbBSeZpW2R7mTK6HD; __Secure-1PAPISID=4vdK4YM32ia-THfm/AbBSeZpW2R7mTK6HD; __Secure-3PAPISID=4vdK4YM32ia-THfm/AbBSeZpW2R7mTK6HD; LOGIN_INFO=AFmmF2swRQIgbOvwQHwhH0c8hszVvHxgqaIFY8dvqtmYb3MKCe3KBRoCIQDK6hgDewaSiFylXs5ohy_ypovpjSCgJGwzJPQqIC4g5g:QUQ3MjNmeWdvTlcxWmlCcDYtbGh2eDUxbERRcVdrYVVRcFFZcFk0QnhDWk9RNnZBQktWMGVvR0JIQmJYcGI4VjNsZ3pjOGhpRThTYlpCelZlcldUc3poSmJ2V0xCWHA2MUlUQmJHb2lGMnhUbTBTSDZTTmQ5dFcwYmxNMVBYbUVadzFWajFpNzVWUlF0M1puRnA1ejJFNFAyY1FwWXRhbUJ3; VISITOR_INFO1_LIVE=8quKZdYJshk; VISITOR_PRIVACY_METADATA=CgJWThIEGgAgKg%3D%3D; PREF=f4=4000000&f6=40000000&tz=Asia.Bangkok&f7=100; SID=g.a000mgiug3lKlPdaV-91bhW-2hwv4qGC_mkfaOMH-4tazTXoWGhReBizPM8og-b5kq6GFPdqoQACgYKAVUSARYSFQHGX2MisVrqRsxECj6WjoDKxhBBORoVAUF8yKpyCfl_W0rzvnVXP9MUHHxG0076; __Secure-1PSID=g.a000mgiug3lKlPdaV-91bhW-2hwv4qGC_mkfaOMH-4tazTXoWGhRVCaxtpv51Dn7tqyd1-Wa0gACgYKAV4SARYSFQHGX2Mi4gspOby7wNB0wRINUmUmBhoVAUF8yKpltLjnaHk1DweXdwy935ME0076; __Secure-3PSID=g.a000mgiug3lKlPdaV-91bhW-2hwv4qGC_mkfaOMH-4tazTXoWGhR1baTuzjxU8FOUTqAzKR5QwACgYKAcQSARYSFQHGX2MieQBUERrXjFD8TVYx0jpLHRoVAUF8yKplVq1IFKSTJTJtNC0mXurZ0076; YSC=oJeM2w_LfP0; __Secure-1PSIDTS=sidts-CjEBUFGoh_SnC3ERL8YMKBOxIT8IaFMi7jeLutnyBxerUjbXql-OSWYvBfbdfOd5c4SKEAA; __Secure-3PSIDTS=sidts-CjEBUFGoh_SnC3ERL8YMKBOxIT8IaFMi7jeLutnyBxerUjbXql-OSWYvBfbdfOd5c4SKEAA; SIDCC=AKEyXzVUNp_bg0vxHE-NpdkTpXPz1o3rjubkAWsXufT9aZ45teOJdIvc-51kEHRnowfM4DpUwWU; __Secure-1PSIDCC=AKEyXzX6Fo5u6Bkt_gFNSPrOlZRCEwTJHyK3K3dNHa9Emuaq0nEBQyLgwQbPj69-lFX2doXD3w; __Secure-3PSIDCC=AKEyXzUO-1WHZV5gmCRygbCMQoNHlk-1bD_n4NbTGiWNzrr7tcGaT41WVrdTmrScZfWjnw3mrg; ST-4n4ru8=session_logininfo=AFmmF2swRQIgbOvwQHwhH0c8hszVvHxgqaIFY8dvqtmYb3MKCe3KBRoCIQDK6hgDewaSiFylXs5ohy_ypovpjSCgJGwzJPQqIC4g5g%3AQUQ3MjNmeWdvTlcxWmlCcDYtbGh2eDUxbERRcVdrYVVRcFFZcFk0QnhDWk9RNnZBQktWMGVvR0JIQmJYcGI4VjNsZ3pjOGhpRThTYlpCelZlcldUc3poSmJ2V0xCWHA2MUlUQmJHb2lGMnhUbTBTSDZTTmQ5dFcwYmxNMVBYbUVadzFWajFpNzVWUlF0M1puRnA1ejJFNFAyY1FwWXRhbUJ3',
        'origin': 'https://www.youtube.com',
        'priority': 'u=1, i',
        'referer': 'https://www.youtube.com/@Relaxingghiblipiano68',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-form-factors': '"Desktop"',
        'sec-ch-ua-full-version': '"127.0.6533.119"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.119", "Chromium";v="127.0.6533.119"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'x-client-data': 'CJW2yQEIpbbJAQipncoBCLyKywEIlKHLAQiFoM0BCLvIzQEIsp7OAQjlr84BCMa2zgEI2rfOARiPzs0BGJyxzgE=',
        'x-goog-authuser': '0',
        'x-goog-visitor-id': 'Cgs4cXVLWmRZSnNoayiamfO1BjIKCgJWThIEGgAgKg%3D%3D',
        'x-origin': 'https://www.youtube.com',
        'x-youtube-bootstrap-logged-in': 'true',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20240813.01.00',
    }
    UIDGET = requests.get(link,headers=headers).json()
    print(UIDGET)
    params = {
        'prettyPrint': 'false',
    }

    json_data = {
        'context': {
            'client': {
                'hl': 'en',
                'gl': 'VN',
                'remoteHost': '2401:d800:f340:105b:f490:36f1:d7ac:759a',
                'deviceMake': '',
                'deviceModel': '',
                'visitorData': 'Cgs4cXVLWmRZSnNoayiamfO1BjIKCgJWThIEGgAgKg%3D%3D',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36,gzip(gfe)',
                'clientName': 'WEB',
                'clientVersion': '2.20240813.01.00',
                'osName': 'Windows',
                'osVersion': '10.0',
                'originalUrl': 'https://www.youtube.com/',
                'screenPixelDensity': 1,
                'platform': 'DESKTOP',
                'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                'configInfo': {
                    'appInstallData': 'CJqZ87UGEKiTsQUQ49GwBRC36v4SEJytsQUQooGwBRC9tq4FEL2KsAUQqJKxBRCQkrEFEIO5_xIQppKxBRCIh7AFEKaasAUQ6sOvBRDbr68FEI6hsQUQ2aWxBRDZya8FEMn3rwUQmZixBRCw7rAFEPSrsAUQtbH_EhDEkrEFEPyFsAUQ1t2wBRDwrLEFENCNsAUQyvmwBRDviLEFEOHssAUQieiuBRCFrrEFEJSJsQUQ7MP_EhCq2LAFEMnXsAUQ2qCxBRDM364FELHcsAUQqJqwBRCinbEFEIjjrwUQ7qKvBRCSnbEFEPirsQUQpcL-EhDvzbAFEIuwsQUQnaawBRDViLAFEJbA_xIQ2a-xBRCWo7EFEOX0sAUQ9quwBRDGpLEFEOKnsQUQyeawBRC9mbAFEJT-sAUQjcywBRDr6P4SEJrwrwUQ0-GvBRCWlbAFELr4sAUQ65mxBRDrk64FEJiNsQUQtaCxBRCPxLAFEOG8_xIQzdewBRDUoa8FEJDGsAUQ3ej-EhCSrrEFEI2UsQUQ3_WwBRDX6a8FEP-IsQUQt--vBRCmk7EFEJ7QsAUQi8-wBRDi1K4FELeUsQUQnrT_EhCq1rAFKhxDQU1TRHhVTW9MMndETkhrQnZQdDhRc2RCdz09',
                },
                'screenDensityFloat': 1.25,
                'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
                'timeZone': 'Asia/Bangkok',
                'browserName': 'Chrome',
                'browserVersion': '127.0.0.0',
                'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'deviceExperimentId': 'ChxOelF3TXpBeE5qZzBPVFU0TWpjMU5qRTBNZz09EJqZ87UGGJqZ87UG',
                'screenWidthPoints': 562,
                'screenHeightPoints': 730,
                'utcOffsetMinutes': 420,
                'connectionType': 'CONN_CELLULAR_4G',
                'memoryTotalKbytes': '8000000',
                'mainAppWebInfo': {
                    'graftUrl': 'https://www.youtube.com/@Relaxingghiblipiano68',
                    'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED',
                    'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                    'isWebNativeShareAvailable': True,
                },
            },
            'user': {
                'lockedSafetyMode': False,
            },
            'request': {
                'useSsl': True,
                'internalExperimentFlags': [],
                'consistencyTokenJars': [],
            },
            'clientScreenNonce': 'N820E3KoLuGpzazh',
            'clickTracking': {
                'clickTrackingParams': 'CCAQmysYASITCI7DhuHl9IcDFXeUSwUdLb8K4zIJY2hhbm5lbHM0',
            },
            'adSignalsInfo': {
                'params': [
                    {
                        'key': 'dt',
                        'value': '1723649182196',
                    },
                    {
                        'key': 'flash',
                        'value': '0',
                    },
                    {
                        'key': 'frm',
                        'value': '0',
                    },
                    {
                        'key': 'u_tz',
                        'value': '420',
                    },
                    {
                        'key': 'u_his',
                        'value': '4',
                    },
                    {
                        'key': 'u_h',
                        'value': '864',
                    },
                    {
                        'key': 'u_w',
                        'value': '1536',
                    },
                    {
                        'key': 'u_ah',
                        'value': '816',
                    },
                    {
                        'key': 'u_aw',
                        'value': '1536',
                    },
                    {
                        'key': 'u_cd',
                        'value': '24',
                    },
                    {
                        'key': 'bc',
                        'value': '31',
                    },
                    {
                        'key': 'bih',
                        'value': '730',
                    },
                    {
                        'key': 'biw',
                        'value': '546',
                    },
                    {
                        'key': 'brdim',
                        'value': '0,0,0,0,1536,0,1536,816,562,730',
                    },
                    {
                        'key': 'vis',
                        'value': '1',
                    },
                    {
                        'key': 'wgl',
                        'value': 'true',
                    },
                    {
                        'key': 'ca_type',
                        'value': 'image',
                    },
                ],
                'bid': 'ANyPxKqdDFpP7653QoTe1i82rBLMWmydy7Y32O-nzZ-vAs1m_Z6qS3DpspeJXkdrDDWRq589BV3bfkxMGAzoeS5_wapltzqduQ',
            },
        },
        'channelIds': [
            'UCLZAQ2tJ0onPYhGW6xsoXHw',
        ],
        'params': 'EgIIAhgA',
    }

    response = requests.post(
        'https://www.youtube.com/youtubei/v1/subscription/subscribe',
        params=params,
        headers=headers,
        json=json_data,
    ).json()
    print(response)
YOUTUBE(61226)

