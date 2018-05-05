;;; try-autoloads.el --- automatically extracted autoloads
;;
;;; Code:


;;;### (autoloads (try try-and-refresh) "try" "try.el" (23277 17620
;;;;;;  519245 746000))
;;; Generated autoloads from try.el

(autoload 'try-and-refresh "try" "\
Refreshes package-list before calling `try'.

\(fn)" t nil)

(autoload 'try "try" "\
Try out a package from your `package-archives' or pass a URL
to a raw .el file. Packages are stored in `try-tmp-dir' and raw
.el files are not stored at all.

\(fn &optional URL-OR-PACKAGE)" t nil)

;;;***

;;;### (autoloads nil nil ("try-pkg.el") (23277 17620 521929 479000))

;;;***

(provide 'try-autoloads)
;; Local Variables:
;; version-control: never
;; no-byte-compile: t
;; no-update-autoloads: t
;; coding: utf-8
;; End:
;;; try-autoloads.el ends here
