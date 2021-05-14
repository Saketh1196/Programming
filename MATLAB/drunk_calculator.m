function drunk_calculator

%% create the body of the calculator

% This is used to set the figure to the desired position 
% set(0, 'DefaultFigureWindowStye, normal)

% to get the screensize of the laptop
monsize = get(0, 'ScreenSize');

% set up the figure. Note that position corresponds to [left,
% bottom, width, height]
calcfig = figure('Position',[200 500 monsize(3)*.25 monsize(4)*.25],'menubar', 'none', 'name','Yes, officer, I''m a Calculator','Numbertitle', 'off');

% fix the size of the calculator and change the background color
set(calcfig,'resize','off','color',[1 0.5 1]*.4); 

figsize = get(calcfig,'Position');
figsize = figsize(3:4);

%% Put some buttons on the body

% locations of the button positions
xfracs = linspace(.1,.5,3);
yfracs = linspace(.6,.1,4);

% Create button for digits for 1-10
for bnum=1:10
    
    h = uicontrol('style', 'pushbutton', 'string', num2str(mod(bnum,10)),...
        'FontSize', 12, 'Callback', @but, 'Position',...
        [xfracs(mod(bnum-1,3)+1)*figsize(1),...
        yfracs(ceil(4*bnum/12))*figsize(2) 70 30]);
end

% buttons for + - * /
symbs = '+-/*';
for si=1:length(symbs)
    
    uicontrol('style', 'pushbutton', 'string', symbs(si),...
        'FontSize', 12, 'Callback', @but, 'Position',...
        [.8*figsize(1), yfracs(si)*figsize(2) 60 30]);
end

% equals sign

uicontrol('style', 'pushbutton', 'string', '=',...
        'FontSize', 12, 'Callback', @but, 'Position',...
        [.3*figsize(1), .1*figsize(2) 100 30]);
    
% clear button

uicontrol('style', 'pushbutton', 'string', 'clear',...
        'FontSize', 12, 'Callback', @but, 'Position',...
        [.6*figsize(1), .1*figsize(2) 65 30]);
    
% display bar
% equals sign

text = uicontrol('style', 'text', 'string', '',...
        'FontSize', 12, 'Callback', @but,'backgroundcolor', [1 1 1]*.2,...
        'HorizontalAlignment', 'right', ....
        'Position',[.1*figsize(1), .8*figsize(2) .86*figsize(1) 30]);


%% Create a blank function

function but(source, ~)
    % flash the color of the calling button
    set(source, 'BackgroundColor',[.3 .4 .8])
    pause(.1)
    set(source, 'BackgroundColor',[1 1 1]*.94)
    
    % update the display so that the pressed button shows up
    whichbutton = get(source,'string');
    displaytext = get(text, 'String');
    
    % if the user clears the screen
    if isequal(whichbutton,'=')
        try
            result = num2str(eval(displaytext));
            set(text,'string',['=' result])
        catch me
            
            set(text,'string', ['=' getaphrase]);
        end
        
    % if user clears the screen   
    elseif isequal(whichbutton,'clear')
        set(text,'string','')
    else
        %clean the display if = is the first character
        if isempty(displaytext) || isequal(displaytext(1),'=')
            set(text,'string',whichbutton);
        else
            % not equal sign; update display
            set(text,'string',[displaytext whichbutton]);
        end
    end
    
end 

function msg = getaphrase
    allmsg = {'oh, I''ve had one too many', 'no, you shut up!'...
        'I''m not drunk, you''re a... wait, what?','I love you man', ...
        'Last call? But I just got here!', 'Calculator? But I hardly know her',...
        'Don''t worry about me, I''ll get home','Tequilla for me? Tequilla for everyone!'};
    msg = allmsg{randi(length(allmsg))};

    
end


end