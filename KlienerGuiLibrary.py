import pygame

pygame.font.init()

def returnKlienerTextCentered(font, fontSize, text, textColor, textPos, uglyFont):
  klienerFont = pygame.font.SysFont(font, fontSize)
  klienerText = klienerFont.render(text, uglyFont, textColor)
  klienerText_rect = klienerText.get_rect(center=textPos)
  return klienerText, klienerText_rect

def returnKlienerText(font, fontSize, text, textColor, textPos, uglyFont):
  klienerFont = pygame.font.SysFont(font, fontSize)
  klienerText = klienerFont.render(text, uglyFont, textColor)
  klienerText_rect = klienerText.get_rect(topleft=textPos)
  return klienerText, klienerText_rect

def drawKlienerTextCentered(font, fontSize, text, textColor, textPos, uglyFont, surface):
  klienerFont = pygame.font.SysFont(font, fontSize)
  klienerText = klienerFont.render(text, uglyFont, textColor)
  klienerText_rect = klienerText.get_rect(center=textPos)
  surface.blit(klienerText, klienerText_rect)

def drawKlienerText(font, fontSize, text, textColor, textPos, uglyFont, surface):
  klienerFont = pygame.font.SysFont(font, fontSize)
  klienerText = klienerFont.render(text, uglyFont, textColor)
  klienerText_rect = klienerText.get_rect(topleft=textPos)
  surface.blit(klienerText, klienerText_rect)