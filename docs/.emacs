;;; package --- Summary
;;; Commentary:

;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.

;;; code:
(package-initialize)
(require 'org)
;;; Treat all themes as safe
(setq custom-safe-themes t)
(org-babel-load-file  (expand-file-name "~/.emacs.d/emacs.org"))
(setq custom-safe-themes t)
(provide '.emacs)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages
   (quote
    (yasnippet which-key use-package try sublime-themes ox-twbs org-bullets org magit jedi htmlize flycheck evil counsel blackboard-theme ace-window))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:background nil))))
 '(aw-leading-char-face ((t (:inherit ace-jump-face-foreground :height 3.0)))))

(autoload 'comint-dynamic-complete-filename "comint" nil t)
(global-set-key(kbd "M-]") 'comint-dynamic-complete-filename)



(desktop-save-mode 1)
(savehist-mode 1)
(add-to-list 'savehist-additional-variables 'kill-ring);; for example
(setq-default message-log-max nil)
(kill-buffer "*Messages*")
(setq initial-scratch-message nil)
(kill-buffer "*scratch*")
(ido-mode 1)
(setq-default fill-column 91)

;; (require 'flycheck)
;; (add-hook 'python-mode-hook 'global-flycheck-mode)

(require 'flymake-python-pyflakes)
(add-hook 'python-mode-hook 'flymake-python-pyflakes-load)

(setq flymake-python-pyflakes-executable "flake8")
(setq flymake-python-pyflakes-extra-arguments '("--ignore='E402'"))


(require 'py-autopep8)
(add-hook 'python-mode-hook 'py-autopep8-enable-on-save)
(bind-key "C-c C-d" 'python-auto-format)
(bind-key "C-c C-d" 'py-autopep8)

(setq make-backup-files nil)

(provide '.emacs)
;;; .emacs ends here
