;; MELPA
(require 'package)
(add-to-list 'package-archives (cons "melpa" "http://melpa.org/packages/") t)

;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.
(package-initialize)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes (quote (tango-dark)))
 '(display-line-numbers-type (quote relative))
 '(doc-view-continuous t)
 '(global-display-line-numbers-mode t)
 '(menu-bar-mode nil)
 '(package-selected-packages
   (quote
    (go-mode markdown-preview-eww haskell-mode eglot markdown-mode use-package latex-preview-pane auctex)))
 '(scroll-bar-mode nil)
 '(tool-bar-mode nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "mononoki" :foundry "UKWN" :slant normal :weight normal :height 98 :width normal)))))

;; (menu-bar-mode 1)
;; (tool-bar-mode -1)
(setq frame-resize-pixelwise t)
(set-face-attribute 'default nil :height 90)
(global-display-line-numbers-mode)

;; transparency
(set-frame-parameter (selected-frame) 'alpha '(90 85))
(add-to-list 'default-frame-alist '(alpha 90 85))

;; LaTeX
(latex-preview-pane-enable)

;; Haskell ghcide
(use-package eglot
  :ensure t
  :config
  (add-to-list 'eglot-server-programs '(haskell-mode . ("ghcide" "--lsp"))))

;; Javacc
(add-to-list 'load-path "~/.emacs.d/lisp/")
(load "javacc-mode.el")

;; Indentation in c/cpp
(setq tab-width 2) 
(defvaralias 'c-basic-offset 'tab-width)
(setq-default c-default-style "linux"
	      c-basic-offset 2)
