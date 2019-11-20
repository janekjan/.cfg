(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes (quote (tango-dark)))
 '(display-line-numbers-type (quote relative))
 '(doc-view-continuous t)
 '(global-display-line-numbers-mode t)
 '(tool-bar-mode nil)
 '(scroll-bar-mode nil)
 '(menu-bar-mode nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "mononoki" :foundry "UKWN" :slant normal :weight normal :height 98 :width normal)))))

;(menu-bar-mode 1)
;(tool-bar-mode -1)
(set-face-attribute 'default nil :height 90)
(global-display-line-numbers-mode)

(set-frame-parameter (selected-frame) 'alpha '(90 85))
(add-to-list 'default-frame-alist '(alpha 90 85))
