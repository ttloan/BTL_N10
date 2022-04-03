USE [QLTP]
GO
/****** Object:  Table [dbo].[Category]    Script Date: 4/3/2022 9:22:49 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Category](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](50) NULL,
	[Image] [text] NULL,
 CONSTRAINT [PK_Category] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Category] ON 

INSERT [dbo].[Category] ([Id], [Name], [Image]) VALUES (1, N'Fresh Food', N'images/category/fresh1.png')
INSERT [dbo].[Category] ([Id], [Name], [Image]) VALUES (2, N'Fruits', N'images/category/fresh2.png')
INSERT [dbo].[Category] ([Id], [Name], [Image]) VALUES (3, N'Vegetable', NULL)
INSERT [dbo].[Category] ([Id], [Name], [Image]) VALUES (4, N'Meats', NULL)
INSERT [dbo].[Category] ([Id], [Name], [Image]) VALUES (5, N'Dried Foods', NULL)
INSERT [dbo].[Category] ([Id], [Name], [Image]) VALUES (6, N'Organic Juices', NULL)
SET IDENTITY_INSERT [dbo].[Category] OFF
GO
