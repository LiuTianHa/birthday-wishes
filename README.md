# 可编辑页面分享应用

这是一个简单的 Web 应用，允许用户创建、编辑和分享自定义页面。

## 功能

1. 创建页面：用户可以创建包含自定义内容的新页面。
2. 编辑页面：用户可以编辑已创建的页面内容。
3. 分享页面：用户可以获取并分享页面的完整 URL。
4. 查看页面：其他人可以通过分享的 URL 查看页面内容。

## 使用方法

1. 访问主页，在文本框中输入初始内容。
2. 点击"创建页面"按钮。
3. 在编辑页面中，可以继续修改内容并保存更改。
4. 复制编辑页面底部显示的完整 URL。
5. 将 URL 分享给他人，他们可以通过该链接查看页面内容。

## 技术说明

- 使用 Flask 框架开发
- 页面内容暂时存储在内存中，重启后会丢失
- 使用 UUID 生成唯一的页面标识符

## 注意事项

- 此应用仅用于演示目的，不适合存储敏感信息
- 由于使用内存存储，数据不会永久保存
- 建议在本地或受控环境中运行此应用

## 部署

1. 确保已安装 Python 和 Flask。
2. 运行 `python main.py` 启动应用。
3. 访问 `http://localhost:5000` 或服务器提供的 URL。

## 未来改进

- 添加数据持久化存储
- 实现用户认证系统
- 增加更多的页面自定义选项
