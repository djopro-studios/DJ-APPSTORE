
function run()
    function split(str, delimiter)
        local result = {}
        local from  = 1
        local delim_from, delim_to = string.find(str, delimiter, from)
        while delim_from do
            table.insert(result, string.sub(str, from, delim_from-1))
            from  = delim_to + 1
            delim_from, delim_to = string.find(str, delimiter, from)
        end
        table.insert(result, string.sub(str, from))
        return result
    end

    win = gui:window()
    title = gui:label(win, 115, 35, 144, 28)
    title:setFontSize(24)
    title:setText("DJ APPSTORE")
    icon = gui:image(win, "icon.png", 65, 25, 20, 20)
    list = gui:image(win, "options.png", 20, 35, 40, 40)

    search = gui:input(win, 35, 65, 50, 10)
    search:setPlaceHolder("Search any apps ...")
    apps = gui:vlist(win, 35, 120, 250, 280)

    -- local up_scroll = gui:image(win,"up.png",290,110,30,30)
    -- local down_scroll = gui:image(win,"down.png",290,450,30,30)

    -- web connecting
    
    -- show apps system
    
    apps_name_data = "SadMan™||SadMan1||SadMan2"
    apps_author_data = "DJOPRO STUDIO||DJ STUDIO||DJSTUDIO"
    apps_desc_data = "An APP that let you to be a sad man||IDK||IDK2"
    apps_icon_data = "data/test.png||data/test.png||data/test.png"-- url des image qui vont etre telecharger
    apps_id_data = "1||2||3"
    apps_n_d = split(apps_name_data, "||")
    apps_a_d = split(apps_author_data, "||")
    apps_d_d = split(apps_desc_data, "||")
    apps_i_d = split(apps_icon_data, "||")
    apps_id = split(apps_id_data, "||")
    
    for i, value in pairs(apps_n_d) do
        local name_app = value
        local desc_app = apps_d_d[i]
        local icon_app = apps_i_d[i]
        local author_app = apps_a_d[i]
        local id_app = apps_id[i]

        _G[id_app.."button"] = gui:label(apps,0,0,100,36)
        _G[id_app.."button"]:setText(name_app)

        _G[id_app.."button"]:onClick(function()

            _G[id_app.."gui"] = gui:window()
            return_ = gui:image(_G[id_app.."gui"], "back.png", 20, 35, 40, 40)
            return_:onClick(function()
                gui:setWindow(win)
            end)
            -- infos of the app
            -- ICON -- DONWLOAD ICON
            
            local icon_app = gui:image(_G[id_app.."gui"], "data/test.png", 50, 70, 100, 100)
            -- END ICON
    
            title = gui:label(_G[id_app.."gui"],170,70,100,36)
            title:setText(name_app) -- TITRE DE l'APP
            title:setFontSize(22)
            title:setHorizontalAlignment(CENTER_ALIGNMENT)
    
            author = gui:label(_G[id_app.."gui"],170,110,100,16)
            author:setText(author_app) -- auteur
            author:setFontSize(15)
            author:setHorizontalAlignment(CENTER_ALIGNMENT)
    
            _G[id_app.."donw_btn"] = gui:button(_G[id_app.."gui"],170,134,100,36)
            _G[id_app.."donw_btn"]:setText("Download")
            
            -- LOADING BAR
            loading_bar = gui:canvas(_G[id_app.."gui"],50,190,0,10,COLOR_WARNING) -- string,int,int,value,int) value to be changed between 0->220
            loading_bar:fillRect(0, 0, 300, 10, COLOR_SUCCESS)
    
            status_text = gui:label(_G[id_app.."gui"],50,205,100,15)
            status_text:setText("")-- status of donwload
            status_text:setFontSize(15)

            -- description
            desc = gui:label(_G[id_app.."gui"],50,260,220,200)
            desc:setText(desc_app) -- this is the description of the app
            desc:setFontSize(16)

            gui:setWindow(_G[id_app.."gui"])
            
            _G[id_app.."donw_btn"]:onClick(function()
                loading_bar:setWidth(10) -- change value from 0 --> 220
                status_text:setText("Downloading ...")
            end)
            -- end 

    
        end)
    end

    list:onClick(function()
        list_win = gui:window()

        return_ = gui:image(list_win, "back.png", 20, 35, 40, 40)
        options = gui:vlist(list_win, 35, 90, 250, 280)
        
        -- options here
        list_list_win = gui:vlist(list_win, 35, 90, 250, 280)

        -- settings options
        settings = gui:box(list_list_win, 0, 0, 250, 36)

        local name = gui:label(settings, 0, 0, 230, 36)
        name:setText("Servers")
        name:setHorizontalAlignment(CENTER_ALIGNMENT)
        name:setFontSize(22)

        local icon = gui:image(settings, "servers.png", 0, 0, 36, 36)

        --exit options

        exit = gui:box(list_list_win, 0, 0, 250, 36)

        local name = gui:label(exit, 0, 0, 230, 36)
        name:setText("exit")
        name:setHorizontalAlignment(CENTER_ALIGNMENT)
        name:setFontSize(22)

        local icon = gui:image(exit, "exit.png", 0, 0, 36, 36)

        --  button actions

        return_:onClick(function()
            gui:setWindow(win)
        end)

        exit:onClick(function()
            gui:setWindow(nil)
            os.exit()
        end)

        settings:onClick(function()
            settings_win = gui:window()

        end)

        -- end
        gui:setWindow(list_win)
    end)
    gui:setWindow(win)
end