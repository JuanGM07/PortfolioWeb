(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[6953,93520],{6953:function(e,r,t){"use strict";var n=t(64836);Object.defineProperty(r,"__esModule",{value:!0}),r.default=void 0;var s=n(t(3848)).default;r.default=s},3848:function(e){"use strict";function lisp(e){!function(e){function simple_form(e){return RegExp(/(\()/.source+"(?:"+e+")"+/(?=[\s\)])/.source)}function primitive(e){return RegExp(/([\s([])/.source+"(?:"+e+")"+/(?=[\s)])/.source)}var r=/(?!\d)[-+*/~!@$%^=<>{}\w]+/.source,t="&"+r,n="(\\()",s="(?=\\s)",a=/(?:[^()]|\((?:[^()]|\((?:[^()]|\((?:[^()]|\((?:[^()]|\([^()]*\))*\))*\))*\))*\))*/.source,i={heading:{pattern:/;;;.*/,alias:["comment","title"]},comment:/;.*/,string:{pattern:/"(?:[^"\\]|\\.)*"/,greedy:!0,inside:{argument:/[-A-Z]+(?=[.,\s])/,symbol:RegExp("`"+r+"'")}},"quoted-symbol":{pattern:RegExp("#?'"+r),alias:["variable","symbol"]},"lisp-property":{pattern:RegExp(":"+r),alias:"property"},splice:{pattern:RegExp(",@?"+r),alias:["symbol","variable"]},keyword:[{pattern:RegExp(n+"(?:and|(?:cl-)?letf|cl-loop|cond|cons|error|if|(?:lexical-)?let\\*?|message|not|null|or|provide|require|setq|unless|use-package|when|while)"+s),lookbehind:!0},{pattern:RegExp(n+"(?:append|by|collect|concat|do|finally|for|in|return)"+s),lookbehind:!0}],declare:{pattern:simple_form(/declare/.source),lookbehind:!0,alias:"keyword"},interactive:{pattern:simple_form(/interactive/.source),lookbehind:!0,alias:"keyword"},boolean:{pattern:primitive(/nil|t/.source),lookbehind:!0},number:{pattern:primitive(/[-+]?\d+(?:\.\d*)?/.source),lookbehind:!0},defvar:{pattern:RegExp(n+"def(?:const|custom|group|var)\\s+"+r),lookbehind:!0,inside:{keyword:/^def[a-z]+/,variable:RegExp(r)}},defun:{pattern:RegExp(n+/(?:cl-)?(?:defmacro|defun\*?)\s+/.source+r+/\s+\(/.source+a+/\)/.source),lookbehind:!0,greedy:!0,inside:{keyword:/^(?:cl-)?def\S+/,arguments:null,function:{pattern:RegExp("(^\\s)"+r),lookbehind:!0},punctuation:/[()]/}},lambda:{pattern:RegExp(n+"lambda\\s+\\(\\s*(?:&?"+r+"(?:\\s+&?"+r+")*\\s*)?\\)"),lookbehind:!0,greedy:!0,inside:{keyword:/^lambda/,arguments:null,punctuation:/[()]/}},car:{pattern:RegExp(n+r),lookbehind:!0},punctuation:[/(?:['`,]?\(|[)\[\]])/,{pattern:/(\s)\.(?=\s)/,lookbehind:!0}]},o={"lisp-marker":RegExp(t),varform:{pattern:RegExp(/\(/.source+r+/\s+(?=\S)/.source+a+/\)/.source),inside:i},argument:{pattern:RegExp(/(^|[\s(])/.source+r),lookbehind:!0,alias:"variable"},rest:i},l="\\S+(?:\\s+\\S+)*",p={pattern:RegExp(n+a+"(?=\\))"),lookbehind:!0,inside:{"rest-vars":{pattern:RegExp("&(?:body|rest)\\s+"+l),inside:o},"other-marker-vars":{pattern:RegExp("&(?:aux|optional)\\s+"+l),inside:o},keys:{pattern:RegExp("&key\\s+"+l+"(?:\\s+&allow-other-keys)?"),inside:o},argument:{pattern:RegExp(r),alias:"variable"},punctuation:/[()]/}};i.lambda.inside.arguments=p,i.defun.inside.arguments=e.util.clone(p),i.defun.inside.arguments.inside.sublist=p,e.languages.lisp=i,e.languages.elisp=i,e.languages.emacs=i,e.languages["emacs-lisp"]=i}(e)}e.exports=lisp,lisp.displayName="lisp",lisp.aliases=[]},64836:function(e){function _interopRequireDefault(e){return e&&e.__esModule?e:{default:e}}e.exports=_interopRequireDefault,e.exports.__esModule=!0,e.exports.default=e.exports}}]);