# 求职项目聊天记录与接续说明

记录日期：2026-10-03。

## 聊天分享链接

[整理27 Summer实习求职方案](https://chatgpt.com/s/cx_6ac17c2231048191a1c156bcd32d18e8)

原消息链接末尾的中文逗号是标点，已从网址中移除。2026-10-03通过浏览器确认可以打开该分享页，页面包含此前的求职调研、材料交付，以及9月30日关于10月2日投递时机的讨论。

## 项目文件

GitHub仓库：[rickx-ri/Job-Finding](https://github.com/rickx-ri/Job-Finding)。本次由用户明确授权上传当前项目文件夹；这不构成投递简历或发送求职消息的授权。

- [项目入口与全部材料](README.md)：跨设备使用时优先读这个文件，链接采用相对路径。
- [交付说明与岗位短名单](reports/delivery_summary.md)
- [岗位表](outputs/recruiting_2027/2027_Internship_Research.xlsx)
- [待确认事项](reports/pending_questions.md)
- [简历版本目录](resumes/manifest.json)

截至2026-09-29的调研覆盖46家公司，保留57条岗位或项目记录，其中22条仅确认学位范围与2027暑期两个条件匹配。完整总简历和D1至D5定向简历、红线及LaTeX源码均已保存。招聘状态是当时的快照，下一次实际投递前需要重新核对；截至本文件建立时，本任务中没有代投递。

## 在另一处Codex继续

克隆仓库后，让新的Codex先读取README.md、本文件和reports/pending_questions.md，再打开上方分享链接。可以使用下面这段提示：

> 请先读取这个仓库中的README.md、CHAT_HISTORY.md、reports/delivery_summary.md及reports/pending_questions.md，再阅读CHAT_HISTORY.md内的聊天分享链接。基于现有资料继续2027暑期实习准备，不推断个人工作授权，不编造研究成果或论文状态。旧岗位状态需要重新核验；未经我明确授权，不投递、不发送求职消息。

## 分享链接与完整历史的区别

分享链接保存的是发布时的只读快照，之后的消息不会自动更新到原链接。官方说明指出，快照可包含用户可见消息和部分文件变更，但不包含原线程的工具调用、Shell命令及工具输入输出；它也不能直接派生出原线程，可以作为附件导入新线程供参考。访问仍取决于链接是否有效以及相应共享权限。[OpenAI官方说明](https://learn.chatgpt.com/docs/use-chatgpt#share-a-read-only-snapshot-of-a-codex-thread)

GitHub保存的是本项目目录的文件，不会自动同步Codex的完整会话。官方列出的本地会话目录通常为`$CODEX_HOME/sessions`和`$CODEX_HOME/archived_sessions`，默认位于`~/.codex/`下；这些目录不在本项目中，也没有随项目上传。[OpenAI历史与日志说明](https://learn.chatgpt.com/docs/reference/troubleshooting#feedback-and-logs)

因此，这个仓库和分享链接可以帮助新的Codex重新了解项目，但不等于完整恢复原任务及其运行状态。仅卸载本地应用与删除本地会话数据是不同操作；若要保留完整本地历史，应先单独做私有备份，不要把整个`~/.codex`目录公开上传。

## 上传范围

仓库保留本项目的简历、PDF、表格、报告、来源快照、脚本及核验文件。本机专用的`scripts/node_modules`符号链接不上传；它指向当前机器上的Codex依赖环境，不是本项目的依赖副本。

部分生成脚本和旧INDEX.md仍含原机器的绝对路径；阅读材料可直接使用README.md，若要在新机器重新生成产物，需要先适配依赖路径。
