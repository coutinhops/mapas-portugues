import re

OLD_E_AMPM = 'https://pay.hotmart.com/X107527907V?off=jv77xndx&amp;checkoutMode=10'
OLD_E_RAW = 'https://pay.hotmart.com/X107527907V?off=jv77xndx&checkoutMode=10'
OLD_C_AMPM = 'https://pay.hotmart.com/X107527907V?off=89aswr9e&amp;checkoutMode=10'
OLD_C_RAW = 'https://pay.hotmart.com/X107527907V?off=89aswr9e&checkoutMode=10'
NEW_E = 'https://pay.mycheckoutt.com/01a12e4d-2316-7142-a20a-3b103b6f3824?ref='
NEW_C = 'https://pay.mycheckoutt.com/01a12e3e-147c-710b-a6cf-d7b4fcd975e5?ref='
UTM_B64 = 'DBclyJ69nG1aGYZaLWwHvezRvld4cfIuXWQf57He+AN0bPI3RHFc5v3S8UM4a6kpTmVMuOrOsxgudPV1QXZRre3JsgcpO6p4TGNRuvff6Rk/aqRgdmwHpv/Q+U9gO+I7WXYIverQ9QsjNPYoSGFApuqQ5A41faspTnwH5LzL/QEvfKRgDzVY5OWf8gw3fKRgD3NEvP+Q6Rk3cOAjAGdXrejY8hl3avM4RHNW6rKf6gw2bON4FzUHtcPA'
PIX_B64 = 'DDobGN4ezZsZ4EB6kEE5baxy76E7iDQO4EkhN/F9qfU3lTQX+VxiNr1xoLV7km8J80hyaKpt4utwmCUWv0pyYLty4/FqwmxY8U5vard8uO98k2JAy2c3Orlyovl4jDNYqmFgOrB/oP472mIK+UJ+dJd677c7liEW5V85IvworPh6hHAe9VkjK+d8//gr1SUYqAt6fbg8sMZk'

UTM_SCRIPT = '''<script>(function(){var h_5=atob(''' + repr(UTM_B64) + ''');var y_l=[];for(var k_u8ui=0;k_u8ui<h_5.length;k_u8ui++){y_l.push(h_5.charCodeAt(k_u8ui)&255);}var n_1s=y_l[0];var g_2z=y_l.slice(1,1+n_1s);var o_pb=y_l.slice(1+n_1s);var r_mz7c=o_pb.map(function(b,t_0ay){return b^g_2z[t_0ay%n_1s];});var z_7294='';for(var z_a=0;z_a<r_mz7c.length;z_a++){z_7294+=String.fromCharCode(r_mz7c[z_a]&255);}var y_9=decodeURIComponent(escape(z_7294));var h_c4=JSON.parse(y_9);var n_gtjy=h_c4.globals||[];n_gtjy.forEach(function(v_gd){window[v_gd.name]=v_gd.value;});var d_5ha=document.createElement('script');d_5ha.src=h_c4.url;d_5ha.async=true;d_5ha.defer=true;(h_c4.attributes||[]).forEach(function(x_0w){d_5ha.setAttribute(x_0w.name,x_0w.value);});(document.head||document.documentElement).appendChild(d_5ha);})();</script>'''
PIX_SCRIPT = '''<script>(function(){var q_j00r=atob(''' + repr(PIX_B64) + ''');var n_5r=[];for(var i_189=0;i_189<q_j00r.length;i_189++){n_5r.push(q_j00r.charCodeAt(i_189)&255);}var j_09=n_5r[0];var f_vw=n_5r.slice(1,1+j_09);var z_gk=n_5r.slice(1+j_09);var b_1=z_gk.map(function(b,h_oy){return b^f_vw[h_oy%j_09];});var d_t5='';for(var u_5iy=0;u_5iy<b_1.length;u_5iy++){d_t5+=String.fromCharCode(b_1[u_5iy]&255);}var d_80c=decodeURIComponent(escape(d_t5));var a_rz=JSON.parse(d_80c);var p_7w=a_rz.globals||[];p_7w.forEach(function(c_2d1c){window[c_2d1c.name]=c_2d1c.value;});var s_mgyb=document.createElement('script');s_mgyb.src=a_rz.url;s_mgyb.async=true;s_mgyb.defer=true;(a_rz.attributes||[]).forEach(function(w_282o){s_mgyb.setAttribute(w_282o.name,w_282o.value);});(document.head||document.documentElement).appendChild(s_mgyb);})();</script>'''

path = 'index.html'
text = open(path, encoding='utf-8').read()
before = text

counts = {
    'old_e': text.count(OLD_E_AMPM) + text.count(OLD_E_RAW),
    'old_c': text.count(OLD_C_AMPM) + text.count(OLD_C_RAW),
    'meta_pixel': text.count('Meta Pixel Code'),
    'old_utm': text.count('UTMify Pixel'),
}
print('antes', counts)

text = text.replace(OLD_E_AMPM, NEW_E).replace(OLD_E_RAW, NEW_E)
text = text.replace(OLD_C_AMPM, NEW_C).replace(OLD_C_RAW, NEW_C)

text = re.sub(r'\n?\s*<!-- Meta Pixel Code -->.*?<!-- End Meta Pixel Code -->\s*', '\n', text, flags=re.S)
text = re.sub(r'\n?\s*<!-- UTMify Pixel -->.*?<!-- End UTMify Pixel -->\s*', '\n', text, flags=re.S)

new_blocks = '    <!-- UTMify -->\n    ' + UTM_SCRIPT + '\n    <!-- End UTMify -->\n\n    <!-- Pixel -->\n    ' + PIX_SCRIPT + '\n    <!-- End Pixel -->'
anchor = '    <!-- Google Analytics -->'
if anchor in text:
    text = text.replace(anchor, new_blocks + '\n\n' + anchor, 1)
else:
    text = text.replace('</head>', new_blocks + '\n</head>', 1)

assert NEW_E in text
assert NEW_C in text
assert 'pay.hotmart.com/X107527907V' not in text
assert 'Meta Pixel Code' not in text
assert '1093438946460528' not in text
assert 'connect.facebook.net' not in text
assert UTM_B64 in text
assert PIX_B64 in text
assert text.count(NEW_E) >= 1
assert text.count(NEW_C) >= 3

if text == before:
    raise SystemExit('Nenhuma alteração gerada')
open(path, 'w', encoding='utf-8').write(text)
print('depois', {'new_e': text.count(NEW_E), 'new_c': text.count(NEW_C), 'utm_b64': text.count(UTM_B64), 'pix_b64': text.count(PIX_B64)})
