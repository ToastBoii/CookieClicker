tcl86t.dll      tk86t.dll       tk              __splash              �  $�  �   �   Xtk86t.dll tk\ttk\cursors.tcl tk\tk.tcl tk\ttk\utils.tcl tk\license.terms tk\ttk\ttk.tcl tk\text.tcl tk\ttk\fonts.tcl tcl86t.dll VCRUNTIME140.dll proc _ipc_server {channel clientaddr clientport} {
set client_name [format <%s:%d> $clientaddr $clientport]
chan configure $channel \
-buffering none \
-encoding utf-8 \
-eofchar \x04 \
-translation cr
chan event $channel readable [list _ipc_caller $channel $client_name]
}
proc _ipc_caller {channel client_name} {
chan gets $channel cmd
if {[chan eof $channel]} {
chan close $channel
exit
} elseif {![chan blocked $channel]} {
if {[string match "update_text*" $cmd]} {
global status_text
set first [expr {[string first "(" $cmd] + 1}]
set last [expr {[string last ")" $cmd] - 1}]
set status_text [string range $cmd $first $last]
}
}
}
set server_socket [socket -server _ipc_server -myaddr localhost 0]
set server_port [fconfigure $server_socket -sockname]
set env(_PYIBoot_SPLASH) [lindex $server_port 2]
image create photo splash_image
splash_image put $_image_data
unset _image_data
proc canvas_text_update {canvas tag _var - -} {
upvar $_var var
$canvas itemconfigure $tag -text $var
}
package require Tk
set image_width [image width splash_image]
set image_height [image height splash_image]
set display_width [winfo screenwidth .]
set display_height [winfo screenheight .]
set x_position [expr {int(0.5*($display_width - $image_width))}]
set y_position [expr {int(0.5*($display_height - $image_height))}]
frame .root
canvas .root.canvas \
-width $image_width \
-height $image_height \
-borderwidth 0 \
-highlightthickness 0
.root.canvas create image \
[expr {$image_width / 2}] \
[expr {$image_height / 2}] \
-image splash_image
wm attributes . -transparentcolor magenta
.root.canvas configure -background magenta
pack .root
grid .root.canvas -column 0 -row 0 -columnspan 1 -rowspan 2
wm overrideredirect . 1
wm geometry . +${x_position}+${y_position}
wm attributes . -topmost 1
raise .�PNG

   IHDR  �   �   	���  �zTXtRaw profile type exif  xڭ�i�㰎���sq'��5bn0ǟ���V��1��e�2E@"�P�Y�����?!�dB�%Ք.~B�5N�u~���+�����}�n���q�s���9������m�ŧ�ʸ}�_���6y�趐�9N�m�z�Ȼ�MЎYW�%?���9λ%��y�Y�~L��9d�7#�s�[��|8���o�$ޝ��������m'8䛟��]���\�D����ÅWg����u�;ߨ��V��v�ޮ{k�͹��=��{�ZH�4݌���g���m�W�7r��Uy����k\�װ�:²m��6���㰃-�\��� 6r����2�'��n�}���7��{���U����t���	��ϼ~�ho�<.z��N��6$r��(b�GQ|��H\=��悁��g��[�#����OZ�<o�"֎l�z"p%�M���ek�c!>��
I�:!�1��.]�>��dm��VǺ��e8�@D�)���
�ɡ��}1�s,�Ɩ|
)��r�k��cN9�knŗPbI%�bJ-���!�XS͵�Z[c��̍�Z��z��^z�m �Fi�Q̨�M7��'f�y�Yg[v�V\i�UV]m��w�q��w�u�GԬ9a�x�}��=jN#%�#jܚ�}
+t%fD�KĳD @;��Ul�H�$fWudEt�2Jp��������>b������_qs��	�"rFB�K�>��%jS8x\�h�$�=�ǀU�+M��_����ew~m��b�{�{��7�`'�9��{N�]�E�#���b�7�����r��F���f�cKrm5?�Xװ:7�b��瞾�n3�W�a��}Չ���*Y��:]iLǔӏ�A��l�UvK��	y_.����ۥh�*}����q����v�]�J�����e$]-v�댹y"�Je��j/��K��Z)�D������#����M��e��CX�`A�jvY��D��������o�
���B�J,8�!w_�8m�!�\��q�|埶A�u4[Yc��&<,�����eu��}[����y��ےm��%�5a*���ɒ��j��q�[����:�L_��$���Q9�pH6>���kF�E�8Cm;�u9ƨ�����,��qwOꔞךܑl!y�n^>b�8Y�<�Y� Z�p��;Bf���_�%�_��2ъu͑�]�I*����v.aΚr��\gۍ�d\��*3mAv��ħ.�Bf% wbb�X���AP���ȿFr�>ʌ�_���3���_�w���I�s�fR�H�� ,1�nB*��ظ6�XyĈ�'��7���ܺ�&#�~��A��������������R��f�#( 
:������]=����4��8;A���0�ؤ�H���E+��Zwo�v�~�J���k����f76)e:�oٔ[����B��M�6+4��{�f�@Q�ƎTd3��{j�$�$�q7�!�NjH��^I��������ۢ�ϫ
U|`���sM�N�Tq�X+�f-"Yp�$,�z������)��"�7U䟎O��%l�n�Zk�T|1����e�#�5�1z��6���F���rO�1�I$%j4t4��f�]>q]�<�%!��5��X�4�D�#�
�뤒���~"$�(�<&�Y����H�$׼���R�q?bp��ȥ�a�K��?%��!E�0ܾ-'L�ڑX�1���C������,�ś]4XƏ0yYӨʴD�F��&R#�(�u�^����jtM�K���LPM�2� �F���V�P�����\��P�� �a���:-�6,gӤ��%@v�Er{�M]�I*UO�Cc6��I��p�'��Q1D!��o�Z-?�����֫�sKi]�\�6�!�^ju�,��4����p�+:�f>W8���1� ���	���:S^i1��;EB �o�o�r�[v��2�v����ڹ�Ii�� ���g�����z�K4Գ�U�sDWf9NOt)�l�./!���%62�u�j��'�`z�\-j%"�� �; ���A<h�\-  �B���@�#�I�^�T-Sp�t$�6�T���$7�F�WKO{2 d��:<T���U��܌���L3@���*g�h��[�@�(�=��$[g��t;��~'ex�_i��:���vf��*�]��Q۽����M��+��
���БkS ykY�m�^�ZL�1����j�iȇt��T�Z��4�%��3s[��/i�kn9-i1.�Z�����Oh���U��LJ�4ID����pϢ������C`-���ֳ�|��?ft7�Ǥ���_|D\J��z42���8���E�Z��'��U��X���- ���B}��6y����Fn�����T7*T����� �u]yt}V6b��F�J;�Z���[�K�#)��:�h	�F�UL{IF`L�]������!��A����֧LK}�@r!\�LTO�?M�Ȍ�rn��%s���O&S�( ��i�'��D�gj���R	>r.H�s��=(��Ȱ�U:`va/lp=h�>�i�~�2>���I�łv�U�p���D�:wL �T����U�N\E�����QH�@�SF��э�� �rq�����EeS(�oU#�����P�*/�J���I�f'�\�J�� M/a��l!�y�N���*��& �	ӣ��v���~\�Z��WZ;y
#}]�0a�X�p����C�J�����*"���wf�uX�pQ��-�!�`n�b�F,-�����G���\l-F��#м�8aT&B�ԇ񟶿X��W��Ư&v0	�}�o��^��HF7�LO;$;rM�k(W�����^�<Ⱥ�6g����df��*h�Yq�����B�W�J�W(�!CI�D�: ��`��tORb�)�YJ�t�9��4�!�l�i�e��K�V����ȯ>��*O� �#L%���3�������j��%��Z�<�s˩��l�����VV�6�j�T-�����:�°"FT�	�v�?"?��M�a��<���i(��rl���>����w�*�n�i�ju�Y��s�xԸ�]zd��S錄�V���(Ѥ�4��}v��2�*_���;Y�]R�� ޭ�H�#��&�,�ly-Y9�y� �N\��%]�r�����Ս:��I�z���[c��^�2�lޗ�àä�����j݌��u=���=�:�|�5?+�/Ț�"[f��u��j$t���>T����E����ͩ�)��x�"�P�3�����m�-�^Ѯ�\�n:.���ڣ��Ne`?20����,Xѥ�>-�qYt��)RK�>��6U��˅3t'C�ӰL˔~�e��Nq=�fw0���&��|�ôNz>izT��m�I!B��;	>����?�����#�*�C��te�N+��h,���8#�@C%��?�ك�P#/�,
ht���5?�3�wc���_���v��E�w���j���3��JB�Dtvh_�
^��09x�P�OS̝(1Qw� �����	�:_���@_��CP�Ȋ��,��v$׺��%�D�9�xW��ɟ����L#�|�h�6Y������ˍ�-�ȟ�=>�5�޲r��ku�����+��D�o)��������ٸk��AR��$��Oe(�-R蛞����"�E�G�5s{B�qJ�9UB�Ŷ�E��W}���}�����1�-v�-ew�8�%[G��Ǥ�*F�k�1�	��#��MXͫ�`'�<
��5����1O���E���&]~���o�|�<A���/�9W��B��  �iCCPICC profile  x�}�=H�@�_S�"U+�t�P�����T�J[�U�K��IC���(��X�:�8���*� �NN�.R���B�X������� �JL5;& U��D4"�3���]D����ǒ�)�_����.̳ڟ�s�*Y��x��E�A<�i���� )����]�����o��<3`���b1��r���O�U�|!���y��Z���=��Ym%�u�AD���!��"J��U#�D��#m�Î?N.�\E0r,������ݚ��I7�:_l�c����m�v��>WZ�_����W�Z���.����\� CO�dH��)�r��}S�z����8} R���pp��){�ͻ�[{��L���,r�W���  �iTXtXML:com.adobe.xmp     <?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="XMP Core 4.4.0-Exiv2">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
    xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:GIMP="http://www.gimp.org/xmp/"
    xmlns:tiff="http://ns.adobe.com/tiff/1.0/"
    xmlns:xmp="http://ns.adobe.com/xap/1.0/"
   xmpMM:DocumentID="gimp:docid:gimp:9c3b37b2-fc16-4147-a750-d00bf1ce158d"
   xmpMM:InstanceID="xmp.iid:54734fb6-2ee5-4868-8e7a-6171c00c9a05"
   xmpMM:OriginalDocumentID="xmp.did:321d0f91-311c-4d43-b73c-fa9080627d4e"
   dc:Format="image/png"
   GIMP:API="2.0"
   GIMP:Platform="Windows"
   GIMP:TimeStamp="1655822518609092"
   GIMP:Version="2.10.24"
   tiff:Orientation="1"
   xmp:CreatorTool="GIMP 2.10">
   <xmpMM:History>
    <rdf:Seq>
     <rdf:li
      stEvt:action="saved"
      stEvt:changed="/"
      stEvt:instanceID="xmp.iid:4a83b477-9a8e-411e-bfb0-f2b622edd521"
      stEvt:softwareAgent="Gimp 2.10 (Windows)"
      stEvt:when="2022-06-21T16:37:48"/>
     <rdf:li
      stEvt:action="saved"
      stEvt:changed="/"
      stEvt:instanceID="xmp.iid:526682b3-2e00-4d43-b5be-8a1363ad092f"
      stEvt:softwareAgent="Gimp 2.10 (Windows)"
      stEvt:when="2022-06-21T16:41:58"/>
    </rdf:Seq>
   </xmpMM:History>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                           
<?xpacket end="w"?>`ɶ�   bKGD � � �����   	pHYs     ��   tIME�):l�ka  IDATx���1�UG�s�m�j�M�����[�4�U,��I����m,lLi���? �0��&��4�B����I�|���ܙ9�<��zv��]^>x���`A����y����ꗕ]f)>�    �  @  �4-������E��ݷ?$}^k     �  @  �
4!j���z�y�sS�u������A�         ��4تԶOk��\��0          Y�m%�n�<|�"��w��hj6�{�?��v&       �  ུ�hZ����Օ��?��&�>���� �  @       \��R�_Qۧ�G���7�qF&       �   �����s��������\m�謞��V�!��         �i��i�כ����ΧU~n�7y���J����b @         �i�F0H�z6Q���       �  `0�ݝo"���A���,�s{i㜞��^��������ۗ
     �  @  s[�_������;` @        �!9�������^���ř?�         ����	���H��P��h�` @         �B��E��Hjk(U��h�` @         �B�EIm���� �  @       4imX-0         ����(":�GKL         @�Z@���T�U��:=o��J�������Ef @         �[@�������ͤ�����^�����Z��\�{����)ݖ��{&       �  ི��z?�'��9<ڟ��	>_�T�ySn�\��>���zY�R�i @         �U�`��}>z�t��wn$}�t;���>;(����J����d @         �nm��5����>��xo�z�z��&       �  �B�������K�g���E��z��d @         
[����Q/o����Q��+��ӓ���o��m~�r����Sי��Zט         `x�Z@���Zm�T��>�����V���u��{�          �S��`��R��Yr����}[��1          �?      �  @  P��p������~c]/���7���f4 �� �  @     X&- >�7R�gߓ��9�d �        ˤ�;J�9�2������=,}��	   �  @     �ĥh�����Z[����L  �     �  `����l����g �� �  @     X&-  �講Z� g(�       �  `Z@\Jk��l�~�&          �jw���6�!Q!���P��^Oj[��}.����Pz�L     �  @  0 g�QZke�g��{7          ��,       �  @              @]�Ϯ|a L         @���y�>�`    IEND�B`�